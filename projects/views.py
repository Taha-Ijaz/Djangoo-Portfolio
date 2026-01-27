from django.shortcuts import render
from .models import Project

def projects_list(request):
    projects = Project.objects.prefetch_related('technologies').order_by('-created_at')
    return render(request, 'projects/projects_list.html', {'projects': projects})