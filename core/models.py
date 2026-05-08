from django.db import models
from django.contrib.auth.models import User

# Modèles existants (Nettoyés et passés en Managed=True)

class StagingAuto(models.Model):
    id_staging_auto = models.AutoField(primary_key=True)
    site = models.CharField(max_length=150, blank=True, null=True)
    code_site = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    pays = models.CharField(max_length=100, blank=True, null=True)
    date_mise_service = models.DateField(blank=True, null=True)
    vehicules = models.CharField(max_length=150, blank=True, null=True)
    anomalies_constatees = models.TextField(blank=True, null=True)
    maintenances_effectuees = models.TextField(blank=True, null=True)
    structure_de_maintenance = models.TextField(blank=True, null=True)
    solutions_proposees = models.TextField(blank=True, null=True)
    etat_de_fonctionnement = models.CharField(max_length=100, blank=True, null=True)
    etat_disponibilite = models.IntegerField(blank=True, null=True)
    tourelle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    laterale = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    acceleration_80kmh = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    vitesse_max_kmh = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tenue_de_route = models.CharField(max_length=50, blank=True, null=True)
    freinage = models.CharField(max_length=50, blank=True, null=True)
    suspection = models.CharField(max_length=50, blank=True, null=True)
    direction = models.CharField(max_length=50, blank=True, null=True)
    annee = models.IntegerField(blank=True, null=True)
    semaine = models.IntegerField(blank=True, null=True)
    categorie_anomalie = models.CharField(max_length=100, blank=True, null=True)
    sous_categorie_anomalie = models.CharField(max_length=100, blank=True, null=True)
    niveau_criticite = models.CharField(max_length=50, blank=True, null=True)
    heure_debut_maintenance = models.TimeField(blank=True, null=True)
    heure_fin_maintenance = models.TimeField(blank=True, null=True)
    date_maintenance = models.DateField(blank=True, null=True)
    duree_maintenance = models.TimeField(blank=True, null=True)
    cout_maintenance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type_maintenance = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'STAGING_AUTO'


class StagingGestionApproAchat(models.Model):
    id_staging = models.AutoField(primary_key=True)
    site = models.CharField(max_length=150, blank=True, null=True)
    service = models.CharField(max_length=150, blank=True, null=True)
    code_magasin = models.CharField(max_length=100, blank=True, null=True)
    nom_magasin = models.CharField(max_length=150, blank=True, null=True)
    code_article = models.CharField(max_length=100, blank=True, null=True)
    libelle_article = models.TextField(blank=True, null=True)
    categorie_article = models.CharField(max_length=150, blank=True, null=True)
    code_fournisseur = models.CharField(max_length=100, blank=True, null=True)
    nom_fournisseur = models.CharField(max_length=200, blank=True, null=True)
    pays_fournisseur = models.CharField(max_length=100, blank=True, null=True)
    type_fournisseur = models.CharField(max_length=150, blank=True, null=True)
    adresse_mail = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=100, blank=True, null=True)
    code_type_achat = models.CharField(max_length=100, blank=True, null=True)
    libelle_type_achat = models.CharField(max_length=150, blank=True, null=True)
    description_type_achat = models.TextField(blank=True, null=True)
    categorie_achat = models.CharField(max_length=150, blank=True, null=True)
    quantite_commandee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantite_recue = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantite_conforme = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantite_entree = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    quantite_sortie = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    prix_unitaire = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    montant_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    delai_livraison = models.IntegerField(blank=True, null=True)
    date_operation = models.DateField(db_column='DATE_OPERATION', blank=True, null=True)
    date_commande = models.DateField(db_column='DATE_COMMANDE', blank=True, null=True)
    code_site = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    direction = models.CharField(max_length=100, blank=True, null=True)
    code_service = models.CharField(max_length=50, blank=True, null=True)
    pays = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'STAGING_GESTION_APPRO_ACHAT'


class StagingMaintenance(models.Model):
    id_staging_maintenance = models.AutoField(db_column='ID_STAGING_MAINTENANCE', primary_key=True)
    date_maintenance = models.DateField(db_column='DATE_MAINTENANCE', blank=True, null=True)
    jour = models.IntegerField(db_column='JOUR', blank=True, null=True)
    mois = models.IntegerField(db_column='MOIS', blank=True, null=True)
    annee = models.IntegerField(db_column='ANNEE', blank=True, null=True)
    semaine = models.IntegerField(db_column='SEMAINE', blank=True, null=True)
    site = models.CharField(db_column='SITE', max_length=100, blank=True, null=True)
    service = models.CharField(db_column='SERVICE', max_length=100, blank=True, null=True)
    systeme = models.CharField(db_column='SYSTEME', max_length=150, blank=True, null=True)
    type_systeme = models.CharField(db_column='TYPE_SYSTEME', max_length=100, blank=True, null=True)
    type_maintenance = models.CharField(db_column='TYPE_MAINTENANCE', max_length=100, blank=True, null=True)
    intervention = models.CharField(db_column='INTERVENTION', max_length=100, blank=True, null=True)
    programme_maintenance = models.CharField(db_column='PROGRAMME_MAINTENANCE', max_length=100, blank=True, null=True)
    user = models.TextField(db_column='USER', blank=True, null=True)
    action_correctrice = models.TextField(db_column='ACTION_CORRECTRICE', blank=True, null=True)
    heure_reception = models.TimeField(db_column='HEURE_RECEPTION', blank=True, null=True)
    heure_constat = models.TimeField(db_column='HEURE_CONSTAT', blank=True, null=True)
    heure_resolution = models.TimeField(db_column='HEURE_RESOLUTION', blank=True, null=True)
    cout_maintenance = models.DecimalField(db_column='COUT_MAINTENANCE', max_digits=12, decimal_places=2, blank=True, null=True)
    statut_maintenance = models.CharField(db_column='STATUT_MAINTENANCE', max_length=50, blank=True, null=True)
    observation = models.TextField(db_column='OBSERVATION', blank=True, null=True)
    duree_maintenance = models.TimeField(db_column='DUREE_MAINTENANCE', blank=True, null=True)
    delai_prise_en_charge = models.TimeField(db_column='DELAI_PRISE_EN_CHARGE', blank=True, null=True)
    direction = models.CharField(db_column='DIRECTION', max_length=100, blank=True, null=True)
    code_service = models.CharField(db_column='CODE_SERVICE', max_length=50, blank=True, null=True)
    code_systeme = models.CharField(db_column='CODE_SYSTEME', max_length=20, blank=True, null=True)
    code_action_correctrice = models.CharField(db_column='CODE_ACTION_CORRECTRICE', max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'STAGING_MAINTENANCE'


class TableDimAnomalie(models.Model):
    id_type_anomalie = models.AutoField(db_column='ID_TYPE_ANOMALIE', primary_key=True)
    code_anomalie = models.CharField(db_column='CODE_ANOMALIE')
    description_panne = models.TextField(db_column='DESCRIPTION_PANNE', blank=True, null=True)
    categorie_anomalie = models.TextField(db_column='CATEGORIE_ANOMALIE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_ANOMALIE'


class TableDimArticle(models.Model):
    id_article = models.AutoField(db_column='ID_ARTICLE', primary_key=True)
    code_article = models.CharField(db_column='CODE_ARTICLE', max_length=10)
    nom_article = models.TextField(db_column='NOM_ARTICLE')
    categorie_article = models.CharField(db_column='CATEGORIE_ARTICLE', max_length=100, blank=True, null=True)
    unite_article = models.CharField(db_column='UNITE_ARTICLE', max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_ARTICLE'


class TableDimCauseIncident(models.Model):
    id_cause = models.AutoField(primary_key=True)
    cause = models.TextField(db_column='CAUSE', blank=True, null=True)
    categorie_cause = models.TextField(db_column='CATEGORIE_CAUSE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_CAUSE_INCIDENT'


class TableDimCriticite(models.Model):
    id_criticite = models.AutoField(db_column='ID_CRITICITE', primary_key=True)
    niveau_criticite = models.TextField(db_column='NIVEAU CRITICITE')

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_CRITICITE'


class TableDimEtatPerformance(models.Model):
    id_etat_performance = models.IntegerField(db_column='ID_ETAT_PERFORMANCE', primary_key=True)
    tenue_route = models.CharField(db_column='TENUE_ROUTE', max_length=50, blank=True, null=True)
    freinage = models.CharField(db_column='FREINAGE', max_length=50, blank=True, null=True)
    suspension = models.CharField(db_column='SUSPENSION', max_length=50, blank=True, null=True)
    direction = models.CharField(db_column='DIRECTION', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_ETAT_PERFORMANCE'


class TableDimFournisseur(models.Model):
    id_fournisseur = models.AutoField(db_column='ID_FOURNISSEUR', primary_key=True)
    code_fournisseur = models.CharField(db_column='CODE_FOURNISSEUR', max_length=20, blank=True, null=True)
    nom_fournisseur = models.TextField(db_column='NOM_FOURNISSEUR')
    pays = models.TextField(db_column='PAYS', blank=True, null=True)
    type_fournisseur = models.TextField(db_column='TYPE_FOURNISSEUR', blank=True, null=True)
    adresse_mail = models.TextField(db_column='ADRESSE_MAIL', blank=True, null=True)
    telephone = models.CharField(db_column='TELEPHONE', max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_FOURNISSEUR'


class TableDimIntervention(models.Model):
    id_intervention = models.AutoField(db_column='ID_INTERVENTION', primary_key=True)
    code_intervention = models.CharField(db_column='CODE_INTERVENTION', max_length=20, blank=True, null=True)
    libelle_intervention = models.CharField(db_column='LIBELLE_INTERVENTION', max_length=100, blank=True, null=True)
    action_intervention = models.TextField(db_column='ACTION_INTERVENTION', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_INTERVENTION'


class TableDimMagasin(models.Model):
    id_magasin = models.AutoField(db_column='ID_MAGASIN', primary_key=True)
    code_magasin = models.CharField(db_column='CODE_MAGASIN', max_length=10)
    nom_magasin = models.TextField(db_column='NOM_MAGASIN', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_MAGASIN'


class TableDimMaintenance(models.Model):
    id_type_maintenance = models.AutoField(db_column='ID_TYPE_MAINTENANCE', primary_key=True)
    code_maintenance = models.CharField(db_column='CODE_MAINTENANCE', max_length=5)
    libelle_maintenance = models.TextField(db_column='LIBELLE_MAINTENANCE')

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_MAINTENANCE'


class TableDimService(models.Model):
    id_service = models.AutoField(db_column='ID_SERVICE', primary_key=True)
    nom_service = models.TextField(db_column='NOM_SERVICE')
    direction = models.TextField(db_column='DIRECTION')
    code_service = models.CharField(db_column='CODE_SERVICE', max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_SERVICE'


class TableDimSite(models.Model):
    id_site = models.AutoField(db_column='ID_SITE', primary_key=True)
    code_site = models.CharField(db_column='CODE_SITE', max_length=10)
    nom_site = models.TextField(db_column='NOM_SITE')
    pays = models.TextField(db_column='PAYS')
    region = models.TextField(db_column='REGION')

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_SITE'


class TableDimSysteme(models.Model):
    id_systeme = models.AutoField(db_column='ID_SYSTEME', primary_key=True)
    code_systeme = models.CharField(db_column='CODE_SYSTEME', max_length=20)
    nom_systeme = models.TextField(db_column='NOM_SYSTEME')
    type_systeme = models.TextField(db_column='TYPE_SYSTEME')

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_SYSTEME'


class TableDimTemps(models.Model):
    id_temps = models.AutoField(db_column='ID_TEMPS', primary_key=True)
    jour = models.IntegerField(db_column='JOUR')
    mois = models.IntegerField(db_column='MOIS')
    semaine = models.IntegerField(db_column='SEMAINE', blank=True, null=True)
    annee = models.IntegerField(db_column='ANNEE')
    date = models.DateField(db_column='DATE')

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_TEMPS'


class TableDimTypeAchat(models.Model):
    id_type_achat = models.AutoField(db_column='ID_TYPE_ACHAT', primary_key=True)
    code_type_achat = models.CharField(db_column='CODE_TYPE_ACHAT', max_length=20, blank=True, null=True)
    libelle_type_achat = models.TextField(db_column='LIBELLE_TYPE_ACHAT')
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    categorie_achat = models.TextField(db_column='CATEGORIE_ACHAT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_TYPE_ACHAT'


class TableDimTypeIncidentSysteme(models.Model):
    id_type_incident = models.AutoField(db_column='ID_TYPE_INCIDENT', primary_key=True)
    libelle_incident = models.TextField(db_column='LIBELLE_INCIDENT', blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    categorie_incident = models.TextField(db_column='CATEGORIE_INCIDENT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_TYPE_INCIDENT_SYSTEME'


class TableDimVehicule(models.Model):
    id_vehicule = models.IntegerField(db_column='ID_VEHICULE', primary_key=True)
    code_vehicule = models.TextField(db_column='CODE_VEHICULE')
    nom_vehicule = models.TextField(db_column='NOM_VEHICULE')
    type_vehicule = models.TextField(db_column='TYPE_VEHICULE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_DIM_VEHICULE'


class TableFaitAnomalieVehicule(models.Model):
    id_anomalie_vehicule = models.AutoField(db_column='ID_ANOMALIE_VEHICULE', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_type_anomalie_table_dim_anomalie = models.ForeignKey(TableDimAnomalie, models.CASCADE, db_column='ID_TYPE_ANOMALIE_TABLE_DIM_ANOMALIE')
    id_vehicule_table_dim_vehicule = models.ForeignKey(TableDimVehicule, models.CASCADE, db_column='ID_VEHICULE_TABLE_DIM_VEHICULE')
    id_criticite_table_dim_criticite = models.ForeignKey(TableDimCriticite, models.CASCADE, db_column='ID_CRITICITE_TABLE_DIM_CRITICITE')
    duree_indisponibilite = models.TimeField(db_column='DUREE_INDISPONIBILITE')

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_ANOMALIE_VEHICULE'


class TableFaitCommande(models.Model):
    id_commande_achat = models.AutoField(db_column='ID_COMMANDE_ACHAT', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_service_table_dim_service = models.ForeignKey(TableDimService, models.CASCADE, db_column='ID_SERVICE_TABLE_DIM_SERVICE')
    id_type_achat_table_dim_type_achat = models.ForeignKey(TableDimTypeAchat, models.CASCADE, db_column='ID_TYPE_ACHAT_TABLE_DIM_TYPE_ACHAT')
    id_fournisseur_table_dim_fournisseur = models.ForeignKey(TableDimFournisseur, models.CASCADE, db_column='ID_FOURNISSEUR_TABLE_DIM_FOURNISSEUR')
    id_article_table_dim_article = models.ForeignKey(TableDimArticle, models.CASCADE, db_column='ID_ARTICLE_TABLE_DIM_ARTICLE')
    quantite_commande = models.IntegerField(db_column='QUANTITE_COMMANDE')
    prix_unitaire = models.DecimalField(db_column='PRIX_UNITAIRE', max_digits=15, decimal_places=2, blank=True, null=True)
    montant_total_commande = models.DecimalField(db_column='MONTANT_TOTAL_COMMANDE', max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_COMMANDE'


class TableFaitIncidentAtm(models.Model):
    id_incident_atm = models.AutoField(db_column='ID_INCIDENT_ATM', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_type_incident_table_dim_type_incident_systeme = models.ForeignKey(TableDimTypeIncidentSysteme, models.CASCADE, db_column='ID_TYPE_INCIDENT_TABLE_DIM_TYPE_INCIDENT_SYSTEME')
    id_criticite_table_dim_criticite = models.ForeignKey(TableDimCriticite, models.CASCADE, db_column='ID_CRITICITE_TABLE_DIM_CRITICITE')
    compte_incident_atm = models.IntegerField(db_column='COMPTE_INCIDENT_ATM', blank=True, null=True)
    heure_detection = models.TimeField(db_column='HEURE_DETECTION')
    heure_resolution = models.TimeField(db_column='HEURE_RESOLUTION')
    duree_incident = models.TimeField(db_column='DUREE_INCIDENT')
    id_cause_table_dim_cause_incident = models.ForeignKey(TableDimCauseIncident, models.SET_NULL, db_column='ID_CAUSE_TABLE_DIM_CAUSE_INCIDENT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_INCIDENT_ATM'


class TableFaitIncidentSysteme(models.Model):
    id_incident_systeme = models.AutoField(db_column='ID_INCIDENT_SYSTEME', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_service_table_dim_service = models.ForeignKey(TableDimService, models.CASCADE, db_column='ID_SERVICE_TABLE_DIM_SERVICE')
    id_systeme_table_dim_systeme = models.ForeignKey(TableDimSysteme, models.CASCADE, db_column='ID_SYSTEME_TABLE_DIM_SYSTEME')
    id_type_incident_table_dim_type_incident_systeme = models.ForeignKey(TableDimTypeIncidentSysteme, models.CASCADE, db_column='ID_TYPE_INCIDENT_TABLE_DIM_TYPE_INCIDENT_SYSTEME')
    id_criticite_table_dim_criticite = models.ForeignKey(TableDimCriticite, models.CASCADE, db_column='ID_CRITICITE_TABLE_DIM_CRITICITE')
    temps_detection = models.TimeField(db_column='TEMPS_DETECTION')
    temps_resolution = models.TimeField(db_column='TEUMPS_RESOLUTION')
    compte_incident_systeme = models.DecimalField(db_column='COMPTE_INCIDENT_SYSTEME', max_digits=10, decimal_places=2, blank=True, null=True)
    duree_indisponibilite = models.TimeField(db_column='DUREE_INDISPONIBILITE')

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_INCIDENT_SYSTEME'


class TableFaitMaintenanceSysteme(models.Model):
    id_fait_maintenance_systeme = models.AutoField(db_column='ID_FAIT_MAINTENANCE_SYSTEME', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_service_table_dim_service = models.ForeignKey(TableDimService, models.CASCADE, db_column='ID_SERVICE_TABLE_DIM_SERVICE')
    id_systeme_table_dim_systeme = models.ForeignKey(TableDimSysteme, models.CASCADE, db_column='ID_SYSTEME_TABLE_DIM_SYSTEME')
    id_type_maintenance_table_dim_maintenance = models.ForeignKey(TableDimMaintenance, models.CASCADE, db_column='ID_TYPE_MAINTENANCE_TABLE_DIM_MAINTENANCE')
    duree_maintenance = models.TimeField(db_column='DUREE_MAINTENANCE')
    cout_maintenance_systeme = models.DecimalField(db_column='COUT_MAINTENANCE_SYSTEME', max_digits=15, decimal_places=2, blank=True, null=True)
    id_intervention_table_dim_intervention = models.ForeignKey(TableDimIntervention, models.SET_NULL, db_column='ID_INTERVENTION_TABLE_DIM_INTERVENTION', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_MAINTENANCE_SYSTEME'


class TableFaitMaintenanceVehicule(models.Model):
    id_maintenance_vehicule = models.AutoField(db_column='ID_MAINTENANCE_VEHICULE', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_vehicule_table_dim_vehicule = models.ForeignKey(TableDimVehicule, models.CASCADE, db_column='ID_VEHICULE_TABLE_DIM_VEHICULE')
    id_type_maintenance_table_dim_maintenance = models.ForeignKey(TableDimMaintenance, models.CASCADE, db_column='ID_TYPE_MAINTENANCE_TABLE_DIM_MAINTENANCE')
    duree_maintenance = models.TimeField(db_column='DUREE_MAINTENANCE')
    cout_maintenance = models.IntegerField(db_column='COUT_MAINTENANCE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_MAINTENANCE_VEHICULE'


class TableFaitPerformanceVehicule(models.Model):
    id_performance = models.AutoField(db_column='ID_PERFORMANCE', primary_key=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_vehicule_table_dim_vehicule = models.ForeignKey(TableDimVehicule, models.CASCADE, db_column='ID_VEHICULE_TABLE_DIM_VEHICULE')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    vitesse_max = models.IntegerField(db_column='VITESSE_MAX')
    laterale = models.IntegerField(db_column='LATERALE', blank=True, null=True)
    tourelle = models.IntegerField(db_column='TOURELLE')
    id_etat_performance_table_dim_etat_performance = models.ForeignKey(TableDimEtatPerformance, models.SET_NULL, db_column='ID_ETAT_PERFORMANCE_TABLE_DIM_ETAT_PERFORMANCE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_PERFORMANCE_VEHICULE'


class TableFaitReceptionAchat(models.Model):
    id_reception = models.AutoField(db_column='ID_RECEPTION', primary_key=True)
    code_reception = models.CharField(db_column='CODE_RECEPTION', max_length=10, blank=True, null=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_service_table_dim_service = models.ForeignKey(TableDimService, models.CASCADE, db_column='ID_SERVICE_TABLE_DIM_SERVICE')
    id_article_table_dim_article = models.ForeignKey(TableDimArticle, models.CASCADE, db_column='ID_ARTICLE_TABLE_DIM_ARTICLE')
    id_fournisseur_table_dim_fournisseur = models.ForeignKey(TableDimFournisseur, models.CASCADE, db_column='ID_FOURNISSEUR_TABLE_DIM_FOURNISSEUR')
    quantite_recue = models.IntegerField(db_column='QUANTITE_RECUE')
    quantite_conforme = models.IntegerField(db_column='QUANTITE_CONFORME')
    delai_livraison = models.IntegerField(db_column='DELAI_LIVRAISON')

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_RECEPTION_ACHAT'


class TableFaitStock(models.Model):
    id_stock = models.AutoField(db_column='ID_STOCK', primary_key=True)
    code_stock = models.CharField(db_column='CODE_STOCK', max_length=10, blank=True, null=True)
    id_temps_table_dim_temps = models.ForeignKey(TableDimTemps, models.CASCADE, db_column='ID_TEMPS_TABLE_DIM_TEMPS')
    id_site_table_dim_site = models.ForeignKey(TableDimSite, models.CASCADE, db_column='ID_SITE_TABLE_DIM_SITE')
    id_magasin_table_dim_magasin = models.ForeignKey(TableDimMagasin, models.CASCADE, db_column='ID_MAGASIN_TABLE_DIM_MAGASIN')
    id_article_table_dim_article = models.ForeignKey(TableDimArticle, models.CASCADE, db_column='ID_ARTICLE_TABLE_DIM_ARTICLE')
    quantite_entree = models.IntegerField(db_column='QUANTITE_ENTREE')
    quantite_sortie = models.IntegerField(db_column='QUANTITE_SORTIE')

    class Meta:
        managed = True
        db_table = 'TABLE_FAIT_STOCK'


class TempProgrammeMaintenance(models.Model):
    systeme = models.TextField(db_column='SYSTEME', blank=True, null=True)
    type_systeme = models.TextField(db_column='TYPE_SYSTEME', blank=True, null=True)
    date_maintenance = models.DateField(db_column='DATE_MAINTENANCE', blank=True, null=True)
    programme_maintenance = models.TextField(db_column='PROGRAMME_MAINTENANCE', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'TEMP_PROGRAMME_MAINTENANCE'


class StagingAts(models.Model):
    id = models.AutoField(primary_key=True) # Corrigé ici
    fir = models.TextField(blank=True, null=True)
    code_site = models.TextField(blank=True, null=True)
    site = models.TextField(blank=True, null=True)
    annee = models.IntegerField(blank=True, null=True)
    date_evenement = models.DateField(blank=True, null=True)
    aeronefs_en_cause = models.TextField(blank=True, null=True)
    trajet = models.TextField(blank=True, null=True)
    zone_occurrence = models.TextField(blank=True, null=True)
    configuration_vol = models.TextField(blank=True, null=True)
    description_evenement = models.TextField(blank=True, null=True)
    type_incident = models.TextField(blank=True, null=True)
    causes = models.TextField(blank=True, null=True)
    heure_detection = models.TimeField(blank=True, null=True)
    heure = models.TextField(blank=True, null=True)
    heure_resolution = models.TimeField(blank=True, null=True)
    duree_incident = models.TimeField(blank=True, null=True)
    criticite = models.TextField(blank=True, null=True)
    compte_incident_atm = models.IntegerField(blank=True, null=True)
    mesures_correctives = models.TextField(blank=True, null=True)
    semaine = models.IntegerField(blank=True, null=True)
    jour = models.IntegerField(blank=True, null=True)
    mois = models.IntegerField(blank=True, null=True)
    pays = models.TextField(blank=True, null=True)
    categorie_causes = models.TextField(blank=True, null=True)
    causes_normalisees = models.TextField(blank=True, null=True)
    categorie_causes_normalisees = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'staging_ats'

# Nouveau modèle UserProfile
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('ADMIN', 'Administrateur'),
        ('USER2', 'Maintenance Systèmes'),
        ('USER3', 'ATM'),
        ('USER4', 'Véhicules'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"