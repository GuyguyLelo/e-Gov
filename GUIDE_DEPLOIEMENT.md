# Guide de deploiement e-Gov (Ubuntu VPS)

Ce guide deploie l'application Django `e-Gov` sur Ubuntu avec PostgreSQL, Gunicorn et Nginx.

## 1) Connexion et prerequis

```bash
ssh root@102.223.179.100
apt update && apt upgrade -y
apt install -y python3 python3-venv python3-pip git nginx postgresql postgresql-contrib
```

## 2) Utilisateur applicatif

```bash
adduser --disabled-password --gecos "" egov
usermod -aG www-data egov
mkdir -p /var/www/egov
chown -R egov:egov /var/www/egov
```

## 3) Cloner le projet

```bash
sudo -u egov -H bash -c "cd /var/www/egov && git clone https://github.com/GuyguyLelo/e-Gov.git app"
```

## 4) Environnement Python et dependances

```bash
sudo -u egov -H bash -c "cd /var/www/egov/app && python3 -m venv venv && . venv/bin/activate && pip install --upgrade pip && pip install django psycopg reportlab gunicorn"
```

## 5) Creer les bases PostgreSQL

```bash
sudo -u postgres psql -c "CREATE DATABASE parametre;"
sudo -u postgres psql -c "CREATE DATABASE kinshasa;"
sudo -u postgres psql -c "CREATE DATABASE kongo_central;"
sudo -u postgres psql -c "CREATE DATABASE police;"
sudo -u postgres psql -c "CREATE USER egov_user WITH PASSWORD 'ChangeMe_Strong_123!';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE parametre TO egov_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE kinshasa TO egov_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE kongo_central TO egov_user;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE police TO egov_user;"
```

## 6) Configurer `.env` (production)

```bash
sudo -u egov -H bash -c "cat > /var/www/egov/app/.env << 'EOF'
DJANGO_DEBUG=false
DJANGO_ALLOWED_HOSTS=102.223.179.100

DB_DEFAULT_ENGINE=django.db.backends.postgresql
DB_DEFAULT_NAME=parametre
DB_DEFAULT_USER=egov_user
DB_DEFAULT_PASSWORD=ChangeMe_Strong_123!
DB_DEFAULT_HOST=localhost
DB_DEFAULT_PORT=5432

DB_KINSHASA_ENGINE=django.db.backends.postgresql
DB_KINSHASA_NAME=kinshasa
DB_KINSHASA_USER=egov_user
DB_KINSHASA_PASSWORD=ChangeMe_Strong_123!
DB_KINSHASA_HOST=localhost
DB_KINSHASA_PORT=5432

DB_KONGO_CENTRAL_ENGINE=django.db.backends.postgresql
DB_KONGO_CENTRAL_NAME=kongo_central
DB_KONGO_CENTRAL_USER=egov_user
DB_KONGO_CENTRAL_PASSWORD=ChangeMe_Strong_123!
DB_KONGO_CENTRAL_HOST=localhost
DB_KONGO_CENTRAL_PORT=5432

DB_POLICE_ENGINE=django.db.backends.postgresql
DB_POLICE_NAME=police
DB_POLICE_USER=egov_user
DB_POLICE_PASSWORD=ChangeMe_Strong_123!
DB_POLICE_HOST=localhost
DB_POLICE_PORT=5432
EOF"
```

## 7) Migrations et statiques

```bash
sudo -u egov -H bash -c "cd /var/www/egov/app && . venv/bin/activate && python manage.py migrate && python manage.py collectstatic --noinput"
```

## 8) Service Gunicorn

```bash
cat > /etc/systemd/system/egov.service << 'EOF'
[Unit]
Description=eGov Gunicorn
After=network.target

[Service]
User=egov
Group=www-data
WorkingDirectory=/var/www/egov/app
Environment="DJANGO_SETTINGS_MODULE=eGov.settings"
ExecStart=/var/www/egov/app/venv/bin/gunicorn eGov.wsgi:application --bind 127.0.0.1:8000 --workers 3 --timeout 120
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable egov
systemctl restart egov
systemctl status egov --no-pager
```

Le paramètre `--timeout 120` (secondes) évite les erreurs `WORKER TIMEOUT` sur les recherches lentes ; la valeur par défaut de Gunicorn est 30 s. Augmentez-la si des requêtes restent trop longues malgré tout.

## 9) Configuration Nginx

```bash
cat > /etc/nginx/sites-available/egov << 'EOF'
server {
    listen 80;
    server_name 102.223.179.100;

    location /static/ {
        alias /var/www/egov/app/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
EOF

ln -s /etc/nginx/sites-available/egov /etc/nginx/sites-enabled/egov
nginx -t
systemctl restart nginx
```

## 10) Firewall et verification

```bash
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable
ufw status

curl -I http://102.223.179.100
journalctl -u egov -n 100 --no-pager
```

## 11) Option HTTPS (si domaine)

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d ton-domaine.com -d www.ton-domaine.com
```

Renouvellement auto:

```bash
systemctl status certbot.timer
```
