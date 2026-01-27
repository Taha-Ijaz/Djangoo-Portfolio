from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'duration')
    search_fields = ('title', 'organization', 'description')
    list_filter = ('organization',)