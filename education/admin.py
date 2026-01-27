from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'duration', 'created_at')
    search_fields = ('degree', 'institution', 'description')
    list_filter = ('institution',)