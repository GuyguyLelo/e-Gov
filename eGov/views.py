from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db import connection, connections
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
from textwrap import wrap
import unicodedata
from io import BytesIO
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas


def normalize(name: str) -> str:
    raw = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
    return raw.replace("_", "").replace(" ", "").lower()


def pretty_label(raw_key: str) -> str:
    label_map = {
        normalize("Naissance"): "Date de naissance",
        normalize("Lieu_Nais"): "Lieu de naissance",
        normalize("Etat_Civil"): "Etat civil",
        normalize("Nom_Père"): "Nom du père",
        normalize("Nom_Mère"): "Nom de la mère",
        normalize("Profession"): "Profession",
        normalize("Province_Origine"): "Province d'origine",
        normalize("Territoire_Origine"): "Territoire d'origine",
        normalize("Sec_Chef_Origine"): "Secteur/Chefferie d'origine",
    }
    key_norm = normalize(raw_key)
    if key_norm in label_map:
        return label_map[key_norm]
    return raw_key.replace("_", " ")


def pretty_value(raw_key: str, value) -> str:
    if value is None:
        return "Non renseigné"
    text = str(value).strip()
    if text == "" or text.lower() == "none":
        return "Non renseigné"
    key_norm = normalize(raw_key)
    # Conversion des codes d'etat civil en libelles lisibles.
    if key_norm == normalize("Etat_Civil"):
        etat_civil_map = {
            "1": "Celibataire",
            "2": "Marie(e)",
            "3": "Divorce(e)",
            "4": "Veuf(ve)",
        }
        code = text[:-2] if text.endswith(".0") else text
        if code in etat_civil_map:
            return etat_civil_map[code]
    # Conversion date ISO -> format francais.
    if key_norm in {normalize("Naissance"), normalize("Date_Nais")}:
        try:
            return datetime.strptime(text[:10], "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            pass
    # Nettoyage telephone: supprimer le .0 final.
    if key_norm in {normalize("Tel"), normalize("Téléphone"), normalize("Telephone")}:
        if text.endswith(".0"):
            return text[:-2]
    return text


def extract_photo_url(values: dict) -> str:
    candidates = ("photo", "photo_url", "image", "image_url", "avatar", "avatar_url")
    for key, value in values.items():
        key_norm = normalize(key)
        if any(normalize(candidate) == key_norm for candidate in candidates):
            if value is None:
                continue
            text = str(value).strip()
            if not text or text.lower() == "none":
                continue
            if text.startswith(("http://", "https://", "/")):
                return text
            return f"/media/{text.lstrip('/')}"
    return ""


def pick_column(columns: list[str], *candidates: str):
    col_map = {normalize(col): col for col in columns}
    for candidate in candidates:
        found = col_map.get(normalize(candidate))
        if found:
            return found
    return None


def resolve_db_alias(province: str) -> str | None:
    if province in connections.databases:
        return province
    upper = province.upper()
    if upper in connections.databases:
        return upper
    return None


def get_allowed_communes(province: str) -> list[str]:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT DISTINCT nom_table
            FROM parametres_databases
            WHERE nom_database = %s
              AND nom_table IS NOT NULL
              AND nom_table <> ''
            ORDER BY nom_table ASC
            """,
            [province],
        )
        return [row[0] for row in cursor.fetchall()]


def resolve_table_name(conn, requested_name: str) -> str | None:
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND lower(table_name) = lower(%s)
            ORDER BY table_name
            LIMIT 1
            """,
            [requested_name],
        )
        row = cursor.fetchone()
    return row[0] if row else None


def build_civil_record(province: str, commune: str, record_id: str):
    allowed_communes = get_allowed_communes(province)
    if commune not in allowed_communes:
        raise Http404("Table non autorisée pour cette province.")

    db_alias = resolve_db_alias(province)
    if not db_alias:
        raise Http404("Base de données province introuvable.")

    conn = connections[db_alias]
    physical_table = resolve_table_name(conn, commune)
    if not physical_table:
        raise Http404("Table introuvable dans la base de la province.")
    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = %s
            """,
            [physical_table],
        )
        columns = [row[0] for row in cursor.fetchall()]
        id_col = pick_column(columns, "ID", "id")
        if not id_col:
            raise Http404("Colonne ID introuvable.")

        q = conn.ops.quote_name
        cursor.execute(
            f"SELECT * FROM {q(physical_table)} WHERE {q(id_col)}::text = %s LIMIT 1",
            [record_id],
        )
        row = cursor.fetchone()
        if not row:
            raise Http404("Enregistrement introuvable.")
        values = dict(zip(columns, row))

    def first_of(*names: str):
        for name in names:
            for col, value in values.items():
                if normalize(col) == normalize(name):
                    return value
        return ""

    def upper_text(value) -> str:
        text = str(value or "").strip()
        return text.upper() if text else ""

    def title_text(value) -> str:
        text = str(value or "").strip()
        return text.capitalize() if text else ""

    record = {
        "id": record_id,
        "nom": upper_text(first_of("Nom", "NOM")),
        "postnom": upper_text(first_of("Postnom", "POSTNOM")),
        "prenom": title_text(first_of("Prénom", "PRENOM", "Prenom")),
        "sexe": first_of("Sexe", "SEXE"),
        "telephone": pretty_value("Téléphone", first_of("Tel", "Téléphone", "TELEPHONE")),
        "adresse": (
            f"{str(first_of('Adresse', 'ADRESSE')).strip()} - {commune}"
            if str(first_of("Adresse", "ADRESSE")).strip()
            else commune
        ),
        "province": province,
        "commune": commune,
        "values": values,
        "photo_url": extract_photo_url(values),
    }

    excluded_norm_keys = {
        normalize("ID"),
        normalize("Nom"),
        normalize("Postnom"),
        normalize("Prénom"),
        normalize("Prenom"),
        normalize("Sexe"),
        normalize("Tel"),
        normalize("Téléphone"),
        normalize("Adresse"),
        normalize("Nom_Ci"),
        normalize("Field14"),
        normalize("Type_Origine"),
    }
    other_values = [
        {"label": pretty_label(key), "value": pretty_value(key, value)}
        for key, value in values.items()
        if normalize(key) not in excluded_norm_keys
    ]

    return record, other_values


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def user_management(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Accès administrateur requis.")
    User = get_user_model()
    success_message = ""
    error_message = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")
        is_admin = request.POST.get("is_admin") == "on"

        if not username:
            error_message = "Le nom d'utilisateur est obligatoire."
        elif len(password) < 6:
            error_message = "Le mot de passe doit contenir au moins 6 caractères."
        elif password != password_confirm:
            error_message = "La confirmation du mot de passe ne correspond pas."
        elif User.objects.filter(username=username).exists():
            error_message = "Ce nom d'utilisateur existe déjà."
        else:
            user = User.objects.create_user(username=username, password=password)
            user.is_staff = is_admin
            user.is_superuser = is_admin
            user.save(update_fields=["is_staff", "is_superuser"])
            success_message = f"Utilisateur {username} créé avec succès."

    users = User.objects.order_by("username")
    return render(
        request,
        "user_management.html",
        {
            "users": users,
            "success_message": success_message,
            "error_message": error_message,
        },
    )


@login_required
def database_management(request):
    if not request.user.is_superuser:
        raise PermissionDenied("Accès administrateur requis.")
    columns = ["nom_database", "nom_table", "domaine"]
    rows = []
    error_message = ""
    success_message = ""

    if request.method == "POST":
        action = request.POST.get("action", "").strip()
        nom_database = request.POST.get("nom_database", "").strip()
        nom_table = request.POST.get("nom_table", "").strip()
        domaine = request.POST.get("domaine", "").strip()
        row_ctid = request.POST.get("row_ctid", "").strip()

        with connection.cursor() as cursor:
            if action == "create":
                if not (nom_database and nom_table):
                    error_message = "Nom database et nom table sont obligatoires."
                else:
                    cursor.execute(
                        """
                        INSERT INTO parametres_databases (nom_database, nom_table, domaine)
                        VALUES (%s, %s, %s)
                        """,
                        [nom_database, nom_table, domaine or None],
                    )
                    success_message = "Enregistrement ajouté avec succès."
            elif action == "update":
                if not row_ctid:
                    error_message = "Ligne introuvable pour modification."
                elif not (nom_database and nom_table):
                    error_message = "Nom database et nom table sont obligatoires."
                else:
                    cursor.execute(
                        """
                        UPDATE parametres_databases
                        SET nom_database = %s, nom_table = %s, domaine = %s
                        WHERE ctid::text = %s
                        """,
                        [nom_database, nom_table, domaine or None, row_ctid],
                    )
                    success_message = "Enregistrement mis à jour avec succès."
            elif action == "delete":
                if not row_ctid:
                    error_message = "Ligne introuvable pour suppression."
                else:
                    cursor.execute(
                        "DELETE FROM parametres_databases WHERE ctid::text = %s",
                        [row_ctid],
                    )
                    success_message = "Enregistrement supprimé avec succès."
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT ctid::text, nom_database, nom_table, domaine
            FROM parametres_databases
            ORDER BY nom_database ASC, nom_table ASC
            """
        )
        rows = [
            {
                "ctid": row[0],
                "nom_database": row[1] or "",
                "nom_table": row[2] or "",
                "domaine": row[3] or "",
            }
            for row in cursor.fetchall()
        ]

    return render(
        request,
        "database_management.html",
        {
            "columns": columns,
            "rows": rows,
            "error_message": error_message,
            "success_message": success_message,
        },
    )


@login_required
def civil_search(request):
    provinces = []
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT DISTINCT nom_database
            FROM parametres_databases
            WHERE nom_database IS NOT NULL AND nom_database <> ''
              AND UPPER(nom_database) <> 'POLICE'
            ORDER BY nom_database ASC
            """
        )
        provinces = [row[0] for row in cursor.fetchall()]

    selected_province = request.GET.get("province", "").strip()
    selected_commune = request.GET.get("commune", "").strip()
    query = request.GET.get("q", "").strip()
    entries = request.GET.get("entries", "10").strip()
    if entries not in {"10", "25", "50", "100"}:
        entries = "10"
    limit = int(entries)
    page = request.GET.get("page", "1").strip()
    try:
        page = max(int(page), 1)
    except ValueError:
        page = 1

    communes = get_allowed_communes(selected_province) if selected_province else []

    rows = []
    total_rows = 0
    total_pages = 0
    offset = (page - 1) * limit
    if selected_province:
        db_alias = resolve_db_alias(selected_province)
        if db_alias:
            conn = connections[db_alias]
            with conn.cursor() as cursor:
                target_communes = []
                if selected_commune:
                    if selected_commune in communes:
                        target_communes = [selected_commune]
                else:
                    target_communes = communes

                quote = conn.ops.quote_name
                union_queries = []
                union_params = []
                tokens = [token for token in query.split() if token]

                for commune_name in target_communes:
                    physical_table = resolve_table_name(conn, commune_name)
                    if not physical_table:
                        continue
                    cursor.execute(
                        """
                        SELECT column_name
                        FROM information_schema.columns
                        WHERE table_schema = 'public' AND table_name = %s
                        """,
                        [physical_table],
                    )
                    columns = [row[0] for row in cursor.fetchall()]
                    if not columns:
                        continue

                    id_col = pick_column(columns, "ID", "id")
                    selected_cols = {
                        "nom": pick_column(columns, "Nom", "NOM", "nom"),
                        "postnom": pick_column(columns, "Postnom", "POSTNOM", "postnom"),
                        "prenom": pick_column(columns, "Prénom", "PRENOM", "Prenom", "prenom"),
                        "sexe": pick_column(columns, "Sexe", "SEXE", "sexe"),
                        "telephone": pick_column(columns, "Tel", "Téléphone", "TELEPHONE", "telephone"),
                        "adresse": pick_column(columns, "Adresse", "ADRESSE", "adresse"),
                    }

                    select_parts = [
                        f'{quote(id_col)}::text AS "id"' if id_col else 'NULL::text AS "id"',
                    ]
                    for alias, real_col in selected_cols.items():
                        if real_col:
                            select_parts.append(f'{quote(real_col)}::text AS "{alias}"')
                        else:
                            select_parts.append(f'NULL::text AS "{alias}"')
                    select_parts.append('%s::text AS "commune"')

                    search_col_names = []
                    for _alias, real_col in selected_cols.items():
                        if real_col and real_col not in search_col_names:
                            search_col_names.append(real_col)
                    if not search_col_names:
                        search_col_names = list(columns)
                    search_parts = [
                        f"COALESCE({quote(col)}::text, '') ILIKE %s" for col in search_col_names
                    ]
                    table_params = [commune_name]
                    where_clause = ""
                    if tokens and search_parts:
                        token_clauses = []
                        for token in tokens:
                            token_clauses.append(f"({' OR '.join(search_parts)})")
                            like = f"%{token}%"
                            table_params.extend([like] * len(search_parts))
                        where_clause = " WHERE " + " AND ".join(token_clauses)

                    union_queries.append(f"SELECT {', '.join(select_parts)} FROM {quote(physical_table)}{where_clause}")
                    union_params.extend(table_params)

                if union_queries:
                    union_sql = " UNION ALL ".join(union_queries)
                    count_sql = f"SELECT COUNT(*) FROM ({union_sql}) AS all_rows"
                    cursor.execute(count_sql, union_params)
                    total_rows = cursor.fetchone()[0] or 0
                    total_pages = (total_rows + limit - 1) // limit if total_rows else 0
                    if total_pages and page > total_pages:
                        page = total_pages
                        offset = (page - 1) * limit

                    data_sql = (
                        f"SELECT id, nom, postnom, prenom, sexe, telephone, adresse, commune "
                        f"FROM ({union_sql}) AS all_rows "
                        f"ORDER BY nom NULLS LAST, postnom NULLS LAST, prenom NULLS LAST "
                        f"LIMIT %s OFFSET %s"
                    )
                    cursor.execute(data_sql, union_params + [limit, offset])
                    fetched = cursor.fetchall()
                    rows = [
                        {
                            "id": row[0] or "",
                            "index": offset + idx,
                            "nom": row[1] or "",
                            "postnom": row[2] or "",
                            "prenom": row[3] or "",
                            "sexe": row[4] or "",
                            "telephone": row[5] or "",
                            "adresse": f"{(row[6] or '').strip()} - {row[7]}" if (row[6] or "").strip() else (row[7] or ""),
                            "commune": row[7] or "",
                            "province_commune": f"{selected_province} / {row[7]}",
                        }
                        for idx, row in enumerate(fetched, start=1)
                    ]

    return render(
        request,
        "civil_search.html",
        {
            "provinces": provinces,
            "communes": communes,
            "selected_province": selected_province,
            "selected_commune": selected_commune,
            "entries": entries,
            "query": query,
            "rows": rows,
            "page": page,
            "total_rows": total_rows,
            "total_pages": total_pages,
            "has_prev": page > 1,
            "has_next": total_pages > page,
            "prev_page": page - 1,
            "next_page": page + 1,
        },
    )


@login_required
def police_search(request):
    query = request.GET.get("q", "").strip()
    entries = request.GET.get("entries", "10").strip()
    if entries not in {"10", "25", "50", "100"}:
        entries = "10"
    limit = int(entries)
    page = request.GET.get("page", "1").strip()
    try:
        page = max(int(page), 1)
    except ValueError:
        page = 1

    rows = []
    total_rows = 0
    total_pages = 0
    offset = (page - 1) * limit

    db_alias = resolve_db_alias("POLICE")
    if db_alias:
        conn = connections[db_alias]
        physical_table = resolve_table_name(conn, "POLICE")
        if physical_table:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_schema = 'public' AND table_name = %s
                    """,
                    [physical_table],
                )
                columns = [row[0] for row in cursor.fetchall()]

                id_col = pick_column(columns, "ID", "id")
                selected_cols = {
                    "nom": pick_column(columns, "Nom", "NOM", "nom"),
                    "postnom": pick_column(columns, "Postnom", "POSTNOM", "postnom"),
                    "prenom": pick_column(columns, "Prénom", "PRENOM", "Prenom", "prenom"),
                    "sexe": pick_column(columns, "Sexe", "SEXE", "sexe"),
                    "telephone": pick_column(columns, "Tel", "Téléphone", "TELEPHONE", "telephone"),
                    "adresse": pick_column(columns, "Adresse", "ADRESSE", "adresse"),
                }

                quote = conn.ops.quote_name
                select_parts = [f'{quote(id_col)}::text AS "_id"' if id_col else 'NULL::text AS "_id"']
                search_parts = []
                for alias, real_col in selected_cols.items():
                    if real_col:
                        select_parts.append(f'{quote(real_col)}::text AS "{alias}"')
                    else:
                        select_parts.append(f'NULL::text AS "{alias}"')

                search_col_names = []
                for _alias, real_col in selected_cols.items():
                    if real_col and real_col not in search_col_names:
                        search_col_names.append(real_col)
                if not search_col_names:
                    search_col_names = list(columns)
                for col in search_col_names:
                    search_parts.append(f"COALESCE({quote(col)}::text, '') ILIKE %s")

                base_sql = f"FROM {quote(physical_table)}"
                params = []
                where_clause = ""
                if query and search_parts:
                    tokens = [token for token in query.split() if token]
                    token_clauses = []
                    for token in tokens:
                        token_clauses.append(f"({' OR '.join(search_parts)})")
                        like = f"%{token}%"
                        params.extend([like] * len(search_parts))
                    where_clause = " WHERE " + " AND ".join(token_clauses)

                count_sql = f"SELECT COUNT(*) {base_sql}{where_clause}"
                cursor.execute(count_sql, params)
                total_rows = cursor.fetchone()[0] or 0
                total_pages = (total_rows + limit - 1) // limit if total_rows else 0
                if total_pages and page > total_pages:
                    page = total_pages
                    offset = (page - 1) * limit

                sql = f"SELECT {', '.join(select_parts)} {base_sql}{where_clause} LIMIT %s OFFSET %s"
                cursor.execute(sql, params + [limit, offset])
                fetched = cursor.fetchall()
                rows = [
                    {
                        "id": row[0] or "",
                        "index": offset + idx,
                        "nom": row[1] or "",
                        "postnom": row[2] or "",
                        "prenom": row[3] or "",
                        "sexe": row[4] or "",
                        "telephone": row[5] or "",
                        "adresse": row[6] or "",
                    }
                    for idx, row in enumerate(fetched, start=1)
                ]

    return render(
        request,
        "police_search.html",
        {
            "entries": entries,
            "query": query,
            "rows": rows,
            "page": page,
            "total_rows": total_rows,
            "total_pages": total_pages,
            "has_prev": page > 1,
            "has_next": total_pages > page,
            "prev_page": page - 1,
            "next_page": page + 1,
        },
    )


def build_police_record(record_id: str):
    province = "POLICE"
    db_alias = resolve_db_alias(province)
    if not db_alias:
        raise Http404("Base de données POLICE introuvable.")

    conn = connections[db_alias]
    physical_table = resolve_table_name(conn, "POLICE")
    if not physical_table:
        raise Http404("Table POLICE introuvable.")

    with conn.cursor() as cursor:
        cursor.execute(
            """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public' AND table_name = %s
            """,
            [physical_table],
        )
        columns = [row[0] for row in cursor.fetchall()]
        id_col = pick_column(columns, "ID", "id")
        if not id_col:
            raise Http404("Colonne ID introuvable.")

        q = conn.ops.quote_name
        cursor.execute(
            f"SELECT * FROM {q(physical_table)} WHERE {q(id_col)}::text = %s LIMIT 1",
            [record_id],
        )
        row = cursor.fetchone()
        if not row:
            raise Http404("Enregistrement introuvable.")
        values = dict(zip(columns, row))

    def first_of(*names: str):
        for name in names:
            for col, value in values.items():
                if normalize(col) == normalize(name):
                    return value
        return ""

    record = {
        "id": record_id,
        "nom": str(first_of("Nom", "NOM") or "").strip().upper(),
        "postnom": str(first_of("Postnom", "POSTNOM") or "").strip().upper(),
        "prenom": str(first_of("Prénom", "PRENOM", "Prenom") or "").strip().capitalize(),
        "sexe": first_of("Sexe", "SEXE"),
        "telephone": pretty_value("Téléphone", first_of("Tel", "Téléphone", "TELEPHONE")),
        "adresse": str(first_of("Adresse", "ADRESSE") or "").strip(),
        "province": province,
        "commune": "POLICE",
    }

    excluded_norm_keys = {
        normalize("ID"),
        normalize("Nom"),
        normalize("Postnom"),
        normalize("Prénom"),
        normalize("Prenom"),
        normalize("Sexe"),
        normalize("Tel"),
        normalize("Téléphone"),
        normalize("Adresse"),
        normalize("F20"),
        normalize("{"),
    }
    other_values = [
        {"label": pretty_label(key), "value": pretty_value(key, value)}
        for key, value in values.items()
        if normalize(key) not in excluded_norm_keys
    ]
    return record, other_values


@login_required
def police_detail(request):
    record_id = request.GET.get("id", "").strip()
    if not record_id:
        raise Http404("Paramètres incomplets.")
    record, other_values = build_police_record(record_id)
    return render(request, "police_detail.html", {"record": record, "other_values": other_values})


@login_required
def police_detail_pdf(request):
    record_id = request.GET.get("id", "").strip()
    if not record_id:
        raise Http404("Paramètres incomplets.")

    record, other_values = build_police_record(record_id)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    p.setTitle(f"{record['nom']} {record['postnom']}".strip() or "Fiche individuelle")

    margin = 1.5 * cm
    top_margin = 2.8 * cm
    content_width = width - 2 * margin
    label_col_w = 6.0 * cm
    value_col_w = content_width - label_col_w
    row_padding = 0.18 * cm
    line_height = 0.38 * cm
    bottom_limit = 2.2 * cm
    current_page = 1
    row_index = 0
    y = height - margin

    def draw_footer():
        today = datetime.now().strftime("%d/%m/%Y")
        p.setStrokeColor(colors.HexColor("#7A8797"))
        p.setLineWidth(1.1)
        p.setFont("Helvetica-Oblique", 8)
        p.line(margin, 1.35 * cm, width - margin, 1.35 * cm)
        p.setFillColor(colors.HexColor("#4A5568"))
        p.drawString(margin, 1.0 * cm, "Document genere automatiquement par e-Gov")
        p.drawCentredString(width / 2, 1.0 * cm, f"Page {current_page}")
        p.drawRightString(width - margin, 1.0 * cm, f"Date du jour: {today}")

    def draw_page_header():
        nonlocal y
        y = height - top_margin
        header_h = 1.4 * cm
        header_bottom = y - header_h + 0.2 * cm
        p.setStrokeColor(colors.HexColor("#3E5A99"))
        p.setFillColor(colors.HexColor("#EAF0FF"))
        p.setLineWidth(1.8)
        p.roundRect(margin, header_bottom, content_width, header_h, 10, stroke=1, fill=1)
        p.setFillColor(colors.HexColor("#1F3C77"))
        y -= 0.6 * cm
        p.setFillColor(colors.HexColor("#1F3C77"))
        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(width / 2, y, "FICHE INDIVIDUELLE")
        y -= 1.45 * cm
        y -= 0.15 * cm

    def draw_table_row(label: str, value: str):
        nonlocal y, current_page, row_index
        value_text = value if value else "-"
        wrapped_value = wrap(str(value_text), width=58) or ["-"]
        row_h = max(0.55 * cm, len(wrapped_value) * line_height + (2 * row_padding))
        if y - row_h < bottom_limit:
            draw_footer()
            p.showPage()
            current_page += 1
            draw_page_header()
        if row_index % 2 == 1:
            p.setFillColor(colors.HexColor("#F5F8FF"))
            p.rect(margin, y - row_h, content_width, row_h, stroke=0, fill=1)
        p.setFillColor(colors.black)
        p.setStrokeColor(colors.HexColor("#4F6287"))
        p.setLineWidth(1.2)
        p.rect(margin, y - row_h, label_col_w, row_h, stroke=1, fill=0)
        p.rect(margin + label_col_w, y - row_h, value_col_w, row_h, stroke=1, fill=0)
        p.setFont("Helvetica-Bold", 9)
        p.drawString(margin + 0.2 * cm, y - row_padding - 0.30 * cm, label)
        is_identity_row = normalize(label) in {normalize("Nom"), normalize("Postnom"), normalize("Prenom"), normalize("Prénom")}
        p.setFont("Helvetica-Bold" if is_identity_row else "Helvetica", 9)
        text_y = y - row_padding - 0.30 * cm
        for line in wrapped_value:
            p.drawString(margin + label_col_w + 0.2 * cm, text_y, line)
            text_y -= line_height
        y -= row_h
        row_index += 1

    draw_page_header()
    rows = [
        ("Nom", record["nom"] or "-"),
        ("Postnom", record["postnom"] or "-"),
        ("Prenom", record["prenom"] or "-"),
        ("Sexe", record["sexe"] or "-"),
        ("Telephone", record["telephone"] or "-"),
        ("Adresse", record["adresse"] or "-"),
    ]
    rows.extend((str(item["label"]), str(item["value"])) for item in other_values)
    for label, value in rows:
        draw_table_row(label, value)
    draw_footer()

    p.showPage()
    p.save()
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    filename = f"{record['nom']}_{record['postnom']}.pdf".replace(" ", "_")
    response["Content-Disposition"] = f'inline; filename="{filename}"'
    return response


@login_required
def civil_detail(request):
    province = request.GET.get("province", "").strip()
    commune = request.GET.get("commune", "").strip()
    record_id = request.GET.get("id", "").strip()
    if not (province and commune and record_id):
        raise Http404("Paramètres incomplets.")

    record, other_values = build_civil_record(province, commune, record_id)
    return render(request, "civil_detail.html", {"record": record, "other_values": other_values})


@login_required
def civil_detail_pdf(request):
    province = request.GET.get("province", "").strip()
    commune = request.GET.get("commune", "").strip()
    record_id = request.GET.get("id", "").strip()
    if not (province and commune and record_id):
        raise Http404("Paramètres incomplets.")

    record, other_values = build_civil_record(province, commune, record_id)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    p.setTitle(f"{record['nom']} {record['postnom']}".strip() or "Fiche individuelle")

    margin = 1.5 * cm
    top_margin = 2.8 * cm
    content_width = width - 2 * margin
    label_col_w = 6.0 * cm
    value_col_w = content_width - label_col_w
    row_padding = 0.18 * cm
    line_height = 0.38 * cm
    bottom_limit = 2.2 * cm
    current_page = 1
    row_index = 0
    y = height - margin

    def draw_footer():
        today = datetime.now().strftime("%d/%m/%Y")
        p.setStrokeColor(colors.HexColor("#7A8797"))
        p.setLineWidth(1.1)
        p.setFont("Helvetica-Oblique", 8)
        p.line(margin, 1.35 * cm, width - margin, 1.35 * cm)
        p.setFillColor(colors.HexColor("#4A5568"))
        p.drawString(margin, 1.0 * cm, "Document genere automatiquement par e-Gov")
        p.drawCentredString(width / 2, 1.0 * cm, f"Page {current_page}")
        p.drawRightString(width - margin, 1.0 * cm, f"Date du jour: {today}")

    def draw_page_header():
        nonlocal y
        y = height - top_margin
        header_h = 1.4 * cm
        header_bottom = y - header_h + 0.2 * cm
        p.setStrokeColor(colors.HexColor("#3E5A99"))
        p.setFillColor(colors.HexColor("#EAF0FF"))
        p.setLineWidth(1.8)
        p.roundRect(margin, header_bottom, content_width, header_h, 10, stroke=1, fill=1)
        p.setFillColor(colors.HexColor("#1F3C77"))
        y -= 0.6 * cm
        p.setFillColor(colors.HexColor("#1F3C77"))
        p.setFont("Helvetica-Bold", 16)
        p.drawCentredString(width / 2, y, "FICHE INDIVIDUELLE")
        y -= 1.45 * cm
        y -= 0.15 * cm

    def draw_table_row(label: str, value: str):
        nonlocal y, current_page, row_index
        value_text = value if value else "-"
        wrapped_value = wrap(str(value_text), width=58) or ["-"]
        row_h = max(0.55 * cm, len(wrapped_value) * line_height + (2 * row_padding))
        if y - row_h < bottom_limit:
            draw_footer()
            p.showPage()
            current_page += 1
            draw_page_header()
        if row_index % 2 == 1:
            p.setFillColor(colors.HexColor("#F5F8FF"))
            p.rect(margin, y - row_h, content_width, row_h, stroke=0, fill=1)
        p.setFillColor(colors.black)
        p.setStrokeColor(colors.HexColor("#4F6287"))
        p.setLineWidth(1.2)
        p.rect(margin, y - row_h, label_col_w, row_h, stroke=1, fill=0)
        p.rect(margin + label_col_w, y - row_h, value_col_w, row_h, stroke=1, fill=0)
        p.setFont("Helvetica-Bold", 9)
        p.drawString(margin + 0.2 * cm, y - row_padding - 0.30 * cm, label)
        is_identity_row = normalize(label) in {normalize("Nom"), normalize("Postnom"), normalize("Prenom"), normalize("Prénom")}
        p.setFont("Helvetica-Bold" if is_identity_row else "Helvetica", 9)
        text_y = y - row_padding - 0.30 * cm
        for line in wrapped_value:
            p.drawString(margin + label_col_w + 0.2 * cm, text_y, line)
            text_y -= line_height
        y -= row_h
        row_index += 1

    draw_page_header()

    rows = [
        ("Nom", record["nom"] or "-"),
        ("Postnom", record["postnom"] or "-"),
        ("Prenom", record["prenom"] or "-"),
        ("Sexe", record["sexe"] or "-"),
        ("Telephone", record["telephone"] or "-"),
        ("Adresse", record["adresse"] or "-"),
        ("Province", record["province"] or "-"),
        ("Commune", record["commune"] or "-"),
    ]
    rows.extend((str(item["label"]), str(item["value"])) for item in other_values)

    for label, value in rows:
        draw_table_row(label, value)

    draw_footer()

    p.showPage()
    p.save()
    buffer.seek(0)

    response = HttpResponse(buffer.getvalue(), content_type="application/pdf")
    filename = f"{record['nom']}_{record['postnom']}.pdf".replace(" ", "_")
    response["Content-Disposition"] = f'inline; filename="{filename}"'
    return response


@login_required
def civil_communes_api(request):
    province = request.GET.get("province", "").strip()
    if not province:
        return JsonResponse({"communes": []})

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT DISTINCT nom_table
            FROM parametres_databases
            WHERE nom_database = %s
              AND nom_table IS NOT NULL
              AND nom_table <> ''
            ORDER BY nom_table ASC
            """,
            [province],
        )
        communes = [row[0] for row in cursor.fetchall()]

    return JsonResponse({"communes": communes})
