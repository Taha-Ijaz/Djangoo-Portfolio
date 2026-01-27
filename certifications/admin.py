from django.contrib import admin
from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'issue_date', 'expiry_date', 'created_at')
    search_fields = ('name', 'organization')
    list_filter = ('organization', 'issue_date')
    date_hierarchy = 'issue_date'
    fieldsets = (
        ('Certification Details', {
            'fields': ('name', 'organization', 'issue_date', 'expiry_date', 'certificate_url')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
