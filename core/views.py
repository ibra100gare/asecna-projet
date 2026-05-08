from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Avg
from .models import *

@login_required
def dashboard_router(request):
    try:
        role = request.user.userprofile.role
    except Exception:
        return render(request, 'login.html', {'error': 'Profil non configuré'})

    if role == 'ADMIN':
        # Calcul des coûts avec gestion des valeurs nulles (None)
        maint_sys = TableFaitMaintenanceSysteme.objects.aggregate(total=Sum('cout_maintenance_systeme'))['total'] or 0
        maint_veh = TableFaitMaintenanceVehicule.objects.aggregate(total=Sum('cout_maintenance'))['total'] or 0
        
        context = {
            'role': role,
            'total_cout_maint': float(maint_sys) + float(maint_veh),
            'total_incidents': TableFaitIncidentSysteme.objects.count() + TableFaitIncidentAtm.objects.count(),
            'total_sites': TableDimSite.objects.count(),
            'total_vehicules': TableDimVehicule.objects.count(),
            'sites_labels': [s.nom_site for s in TableDimSite.objects.all()[:5]],
            'incidents_data': [TableFaitIncidentSysteme.objects.filter(id_site_table_dim_site=s).count() for s in TableDimSite.objects.all()[:5]],
            # Correction : order_by au lieu de order_all
            'recent_commandes': TableFaitCommande.objects.select_related('id_article_table_dim_article', 'id_site_table_dim_site').all().order_by('-id_commande_achat')[:10]
        }
        return render(request, 'dashboards/admin.html', context)

    elif role == 'USER2':
        # Dashboard Maintenance Systèmes
        context = {
            'role': role,
            'cout_systemes': TableFaitMaintenanceSysteme.objects.aggregate(total=Sum('cout_maintenance_systeme'))['total'] or 0,
            'nb_interventions': TableFaitMaintenanceSysteme.objects.count(),
            'maintenances': TableFaitMaintenanceSysteme.objects.select_related('id_systeme_table_dim_systeme', 'id_site_table_dim_site').all().order_by('-id_fait_maintenance_systeme')[:15],
        }
        return render(request, 'dashboards/maintenance.html', context)

    # --- 3. DASHBOARD USER3 (ATM - AIR TRAFFIC MANAGEMENT) ---
    elif role == 'USER3':
        # Statistiques par criticité pour un graphique Camembert (Pie Chart)
        stats_crit = TableFaitIncidentAtm.objects.values(
            'id_criticite_table_dim_criticite__niveau_criticite'
        ).annotate(total=Count('id_incident_atm'))

        context = {
            'role': 'Gestion ATM',
            'nb_incidents_atm': TableFaitIncidentAtm.objects.count(),
            # Liste des incidents ATM
            'incidents': TableFaitIncidentAtm.objects.select_related(
                'id_site_table_dim_site', 
                'id_type_incident_table_dim_type_incident_systeme',
                'id_criticite_table_dim_criticite'
            ).all().order_by('-id_incident_atm')[:15],
            'labels_crit': [item['id_criticite_table_dim_criticite__niveau_criticite'] for item in stats_crit],
            'data_crit': [item['total'] for item in stats_crit],
        }
        return render(request, 'dashboards/atm.html', context)

    # --- 4. DASHBOARD USER4 (VÉHICULES & PARC AUTO) ---
    elif role == 'USER4':
        context = {
            'role': 'Maintenance Véhicules',
            'nb_vehicules': TableDimVehicule.objects.count(),
            'cout_maint_v': TableFaitMaintenanceVehicule.objects.aggregate(total=Sum('cout_maintenance'))['total'] or 0,
            # Liste des anomalies constatées
            'anomalies': TableFaitAnomalieVehicule.objects.select_related(
                'id_vehicule_table_dim_vehicule', 
                'id_type_anomalie_table_dim_anomalie',
                'id_criticite_table_dim_criticite'
            ).all().order_by('-id_anomalie_vehicule')[:12],
            # Performances récentes
            'performances': TableFaitPerformanceVehicule.objects.select_related(
                'id_vehicule_table_dim_vehicule',
                'id_site_table_dim_site'
            ).all().order_by('-id_performance')[:8]
        }
        return render(request, 'dashboards/vehicules.html', context)

    # Par défaut, si aucun rôle ne correspond
    return redirect('login')