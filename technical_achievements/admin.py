from django.contrib import admin
from .models import TechnicalAchievement

@admin.register(TechnicalAchievement)
class TechnicalAchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('order',)
    list_editable = ('order',)
    fieldsets = (
        ('Achievement Details', {
            'fields': ('title', 'description', 'icon', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)
    help_texts = {
        'icon': 'Font Awesome icon class (e.g., fas fa-code, fas fa-trophy, fas fa-certificate)'
    }
