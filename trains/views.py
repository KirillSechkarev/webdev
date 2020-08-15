from django.shortcuts import render
from .models import Train
from django.core.paginator import Paginator

def home(request):
    trains = Train.objects.all()
    paginator = Paginator(trains, 2)
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'trains/home.html', {'object_list': trains})
