from django.shortcuts import render
from .models import Drug
from django.db.models import Q
from datetime import date

# Create your views here.

def index(request):
    get_data = request.GET 
    if get_data.get('filter_type') == 'search':
        value = get_data.get("filter_value")
        drugs = Drug.objects.filter(Q(title__icontains=value) | Q(factory__title__icontains=value))
    else:
        drugs = Drug.objects.all().order_by('-price')

    return render(request, 'index.html', context={'drugs': drugs})





    