from django.shortcuts import render
from .models import Experience

def experience_list(request):
    experiences = Experience.objects.order_by('-start_date', '-end_date')
    return render(request, 'experience/experience_list.html', {'experiences': experiences})