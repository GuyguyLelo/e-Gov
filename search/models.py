from django.db import models

class Databases(models.Model):
    nom_database = models.TextField(max_length=500, blank=True)
    nom_table = models.TextField(max_length=500, blank=True)
    domaine = models.TextField(max_length=500, blank=True)


#####################################################################DATA BASE KINSHASA


class Bumbu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)  # Field name made lowercase.
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.FloatField(db_column='Tel', blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bumbu'


class Gombe(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)  # Field name made lowercase.
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.FloatField(db_column='Tel', blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gombe'


class Kalamu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)  # Field name made lowercase.
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kalamu'


class KasaVubu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)  # Field name made lowercase.
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kasa_Vubu'


class Kimbanseke(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)  # Field name made lowercase.
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)  # Field name made lowercase.
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)  # Field name made lowercase.
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Kimbanseke'


class Bandalungwa(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bandalungwa'


class Barumbu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Barumbu'


class Kasa_Vubu(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kasa_Vubu'


class Kinshasa(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kinshasa'


#####################################################################DATA BASE KONGO CENTRAL

class BomaVille(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Boma Ville'


class Kasangulu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kasangulu'


class MatadiVille(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Matadi ville'


class Tshela(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TSHELA'


#####################################################################DATA BASE POLICE

class Police(models.Model):
    serie = models.CharField(db_column='Serie', max_length=255, blank=True, null=True)
    ancien_matr = models.CharField(db_column='ANCIEN_MATR', max_length=255, blank=True, null=True)
    matricule = models.CharField(db_column='MATRICULE', max_length=255, blank=True, null=True)
    nom_postnom = models.CharField(db_column='NOM_POSTNOM', max_length=255, blank=True, null=True)
    nom = models.CharField(db_column='NOM', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='POSTNOM', max_length=255, blank=True, null=True)
    prenom = models.CharField(db_column='PRENOM', max_length=255, blank=True, null=True)
    grade = models.CharField(db_column='GRADE', max_length=255, blank=True, null=True)
    date_nais = models.CharField(db_column='DATE_NAIS', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='LIEU_NAIS', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='SEXE', max_length=10, blank=True, null=True)
    fonction = models.CharField(db_column='FONCTION', max_length=255, blank=True, null=True)
    unite = models.CharField(db_column='UNITE', max_length=255, blank=True, null=True)
    dept_bn_distr_gp = models.CharField(db_column='DEPT_BN_DISTR_GP', max_length=255, blank=True, null=True)
    province_or = models.CharField(db_column='PROVINCE_OR', max_length=255, blank=True, null=True)
    district_or = models.CharField(db_column='DISTRICT_OR', max_length=255, blank=True, null=True)
    territoire_or = models.CharField(db_column='TERRITOIRE_OR', max_length=255, blank=True, null=True)
    secteur_or = models.CharField(db_column='SECTEUR_OR', max_length=255, blank=True, null=True)
    village_or = models.CharField(db_column='VILLAGE_OR', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Police'


class Kintambo(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kintambo'


class Kisenso(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kisenso'


class Lemba(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lemba'


class Limete(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Limete'


class Makala(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Makala'


class Maluku(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Maluku'


class Masina(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Masina'


class Matete(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Matete'


class MontNgafula(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mont_Ngafula'


class Ndjili(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ndjili'


class Ngaba(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ngaba'


class Ngaliema(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ngaliema'


class NgiriNgiri(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ngiri_Ngiri'


class Nsele(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nsele'


class Selembao(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Selembao'


class Mont_Ngafula(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mont_Ngafula'


class Ngiri_Ngiri(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field14 = models.CharField(db_column='Field14', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ngiri_Ngiri'


class Kimvula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kimvula'


class Lukula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lukula'


class Luozi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Luozi'


class Madimba(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Madimba'


class MbanzaNgungu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mbanza Ngungu'


class Moanda(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.FloatField(db_column='Tel', blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Moanda'


class SekeBanza(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.CharField(db_column='Naissance', max_length=255, blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SEKE BANZA'


class Songololo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SONGOLOLO'


class Bagata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nom = models.CharField(db_column='Nom', max_length=255, blank=True, null=True)
    postnom = models.CharField(db_column='Postnom', max_length=255, blank=True, null=True)
    prénom = models.CharField(db_column='Prénom', max_length=255, blank=True, null=True)
    sexe = models.CharField(db_column='Sexe', max_length=255, blank=True, null=True)
    naissance = models.DateTimeField(db_column='Naissance', blank=True, null=True)
    lieu_nais = models.CharField(db_column='Lieu_Nais', max_length=255, blank=True, null=True)
    etat_civil = models.FloatField(db_column='Etat_Civil', blank=True, null=True)
    nom_père = models.CharField(db_column='Nom_Père', max_length=255, blank=True, null=True)
    nom_mère = models.CharField(db_column='Nom_Mère', max_length=255, blank=True, null=True)
    tel = models.CharField(db_column='Tel', max_length=255, blank=True, null=True)
    profession = models.CharField(db_column='Profession', max_length=255, blank=True, null=True)
    adresse = models.CharField(db_column='Adresse', max_length=255, blank=True, null=True)
    sec_chef_com_résidence = models.CharField(db_column='Sec_Chef_Com_Résidence', max_length=255, blank=True, null=True)
    type_résidence = models.CharField(db_column='Type_Résidence', max_length=255, blank=True, null=True)
    group_q_résidence = models.CharField(db_column='Group_Q_Résidence', max_length=255, blank=True, null=True)
    nom_ci = models.CharField(db_column='Nom_Ci', max_length=255, blank=True, null=True)
    field17 = models.CharField(db_column='Field17', max_length=255, blank=True, null=True)
    province_origine = models.CharField(db_column='Province_Origine', max_length=255, blank=True, null=True)
    territoire_origine = models.CharField(db_column='Territoire_Origine', max_length=255, blank=True, null=True)
    sec_chef_origine = models.CharField(db_column='Sec_Chef_Origine', max_length=255, blank=True, null=True)
    type_origine = models.CharField(db_column='Type_Origine', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bagata'