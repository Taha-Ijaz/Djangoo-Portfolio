from django.shortcuts import render
from .models import Education

def education_list(request):
    educations = Education.objects.order_by('-start_date', '-end_date')
    return render(request, 'education/education_list.html', {'educations': educations})