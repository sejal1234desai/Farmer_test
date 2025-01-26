from django.contrib import admin


from django.contrib import admin
from .models import Farmer, TreeSpecies, ImplementationDetail, TeamMember

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'plot_location')
    search_fields = ('name', 'contact')

@admin.register(TreeSpecies)
class TreeSpeciesAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'species_name', 'quantity')
    search_fields = ('species_name',)

@admin.register(ImplementationDetail)
class ImplementationDetailAdmin(admin.ModelAdmin):
    list_display = ('farmer', 'notes')
    search_fields = ('farmer__name',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role')
