from django.contrib import admin
from .models import Portfolio, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_at', 'updated_at')
    search_fields = ('project_name',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'portfolio_title', 'user', 'project')
    search_fields = ('portfolio_title', 'user__first_name', 'user__last_name')
    raw_id_fields = ('user', 'project')