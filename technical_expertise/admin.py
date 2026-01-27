from django.contrib import admin
from .models import TechnicalExpertise

@admin.register(TechnicalExpertise)
class TechnicalExpertiseAdmin(admin.ModelAdmin):
    list_display = ('category', 'order', 'created_at')
    search_fields = ('category', 'description')
    list_filter = ('order',)
    list_editable = ('order',)
    fieldsets = (
        ('Expertise Details', {
            'fields': ('category', 'description', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
