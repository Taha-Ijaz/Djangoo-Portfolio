from django.shortcuts import render
from bio.models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def home(request):
    bio = Bio.objects.order_by('-updated_at').first()
    educations = Education.objects.order_by('-start_date', '-end_date')
    skills = Skill.objects.order_by('category', 'name')
    experiences = Experience.objects.order_by('-start_date', '-end_date')
    projects = Project.objects.prefetch_related('technologies').order_by('-created_at')

    context = {
        'bio': bio,
        'educations': educations,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
    }
    return render(request, 'core/index.html', context)