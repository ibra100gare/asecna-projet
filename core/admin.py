from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# ==============================================================================
# 1. GESTION DES UTILISATEURS ET PROFILS
# ==============================================================================

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profils Utilisateurs (Rôles)'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')

    def get_role(self, obj):
        return obj.userprofile.role if hasattr(obj, 'userprofile') else None
    get_role.short_description = 'Rôle'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# ==============================================================================
# 2. TABLES DE STAGING (Données Brutes / Import)
# ==============================================================================

@admin.register(StagingAts)
class StagingAtsAdmin(admin.ModelAdmin):
    list_display = ('id', 'site', 'annee', 'date_evenement', 'type_incident', 'criticite')
    list_filter = ('annee', 'pays', 'criticite')
    search_fields = ('site', 'description_evenement')

@admin.register(StagingAuto)
class StagingAutoAdmin(admin.ModelAdmin):
    list_display = ('vehicules', 'site', 'date_maintenance', 'cout_maintenance', 'etat_de_fonctionnement')
    list_filter = ('region', 'pays', 'etat_de_fonctionnement')
    search_fields = ('vehicules', 'anomalies_constatees')

@admin.register(StagingMaintenance)
class StagingMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('systeme', 'site', 'date_maintenance', 'type_maintenance', 'statut_maintenance')
    list_filter = ('annee', 'site', 'statut_maintenance')
    search_fields = ('systeme', 'intervention')

@admin.register(StagingGestionApproAchat)
class StagingApproAdmin(admin.ModelAdmin):
    list_display = ('libelle_article', 'nom_fournisseur', 'date_commande', 'montant_total', 'site')
    list_filter = ('pays', 'categorie_achat', 'region')
    search_fields = ('libelle_article', 'nom_fournisseur')

# ==============================================================================
# 3. TABLES DE DIMENSIONS (Référentiels)
# ==============================================================================

@admin.register(TableDimSite)
class TableDimSiteAdmin(admin.ModelAdmin):
    list_display = ('code_site', 'nom_site', 'pays', 'region')
    search_fields = ('nom_site', 'code_site')

@admin.register(TableDimSysteme)
class TableDimSystemeAdmin(admin.ModelAdmin):
    list_display = ('code_systeme', 'nom_systeme', 'type_systeme')
    search_fields = ('nom_systeme', 'code_systeme')

@admin.register(TableDimVehicule)
class TableDimVehiculeAdmin(admin.ModelAdmin):
    list_display = ('code_vehicule', 'nom_vehicule', 'type_vehicule')
    search_fields = ('nom_vehicule', 'code_vehicule')

@admin.register(TableDimArticle)
class TableDimArticleAdmin(admin.ModelAdmin):
    list_display = ('code_article', 'nom_article', 'categorie_article', 'unite_article')
    search_fields = ('nom_article', 'code_article')

@admin.register(TableDimFournisseur)
class TableDimFournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom_fournisseur', 'pays', 'type_fournisseur', 'telephone')
    search_fields = ('nom_fournisseur', 'code_fournisseur')

@admin.register(TableDimService)
class TableDimServiceAdmin(admin.ModelAdmin):
    list_display = ('nom_service', 'direction', 'code_service')

# Enregistrement simple pour les petites dimensions
admin.site.register([
    TableDimAnomalie, TableDimCauseIncident, TableDimCriticite, 
    TableDimEtatPerformance, TableDimIntervention, TableDimMagasin, 
    TableDimMaintenance, TableDimTemps, TableDimTypeAchat, 
    TableDimTypeIncidentSysteme
])

# ==============================================================================
# 4. TABLES DE FAITS (Données Métier Centrales)
# ==============================================================================

@admin.register(TableFaitMaintenanceSysteme)
class FaitMaintenanceSystemeAdmin(admin.ModelAdmin):
    list_display = ('id_fait_maintenance_systeme', 'id_systeme_table_dim_systeme', 'id_site_table_dim_site', 'cout_maintenance_systeme', 'duree_maintenance')
    list_filter = ('id_site_table_dim_site', 'id_type_maintenance_table_dim_maintenance')
    # Les ForeignKey utilisent select_related pour éviter de ralentir la base
    list_select_related = ('id_systeme_table_dim_systeme', 'id_site_table_dim_site')

@admin.register(TableFaitIncidentAtm)
class FaitIncidentAtmAdmin(admin.ModelAdmin):
    list_display = ('id_incident_atm', 'id_site_table_dim_site', 'id_criticite_table_dim_criticite', 'heure_detection', 'duree_incident')
    list_filter = ('id_site_table_dim_site', 'id_criticite_table_dim_criticite')

@admin.register(TableFaitIncidentSysteme)
class FaitIncidentSystemeAdmin(admin.ModelAdmin):
    list_display = ('id_incident_systeme', 'id_systeme_table_dim_systeme', 'id_site_table_dim_site', 'duree_indisponibilite')
    list_filter = ('id_site_table_dim_site', 'id_criticite_table_dim_criticite')

@admin.register(TableFaitMaintenanceVehicule)
class FaitMaintenanceVehiculeAdmin(admin.ModelAdmin):
    list_display = ('id_maintenance_vehicule', 'id_vehicule_table_dim_vehicule', 'id_site_table_dim_site', 'cout_maintenance')
    list_filter = ('id_site_table_dim_site', 'id_type_maintenance_table_dim_maintenance')

@admin.register(TableFaitCommande)
class FaitCommandeAdmin(admin.ModelAdmin):
    list_display = ('id_commande_achat', 'id_article_table_dim_article', 'id_fournisseur_table_dim_fournisseur', 'quantite_commande', 'montant_total_commande')
    list_filter = ('id_site_table_dim_site', 'id_service_table_dim_service')

@admin.register(TableFaitStock)
class FaitStockAdmin(admin.ModelAdmin):
    list_display = ('id_stock', 'id_article_table_dim_article', 'id_magasin_table_dim_magasin', 'quantite_entree', 'quantite_sortie')
    list_filter = ('id_site_table_dim_site', 'id_magasin_table_dim_magasin')

@admin.register(TableFaitPerformanceVehicule)
class FaitPerformanceVehiculeAdmin(admin.ModelAdmin):
    list_display = ('id_performance', 'id_vehicule_table_dim_vehicule', 'vitesse_max', 'laterale', 'tourelle')
    list_filter = ('id_site_table_dim_site',)

# Enregistrement des tables restantes
admin.site.register(TableFaitAnomalieVehicule)
admin.site.register(TableFaitReceptionAchat)
admin.site.register(TempProgrammeMaintenance)