from django.contrib import admin
from .models import Project, Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_link', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('technologies',)
    filter_horizontal = ('technologies',)