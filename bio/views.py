from django.shortcuts import render
from .models import Bio

def bio_detail(request):
    bio = Bio.objects.order_by('-updated_at').first()
    return render(request, 'bio/bio_detail.html', {'bio': bio})