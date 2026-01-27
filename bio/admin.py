from django.contrib import admin
from .models import Bio

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'updated_at')
    search_fields = ('full_name', 'job_title', 'description', 'email')
    readonly_fields = ('created_at', 'updated_at')