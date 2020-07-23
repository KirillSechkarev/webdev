from django.shortcuts import render
from .models import City
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CityForm
from django.urls import reverse_lazy


def home(request):
    if request.method == 'POST':
        # form = HtmlForm(request.POST or None)
        form = CityForm(request.POST or None)
        if form.is_valid(): # Проверка на валидность
            print(form.cleaned_data)
    # form = HtmlForm()
    form = CityForm()
    # print(request.POST)
    city = request.POST.get("name")
    # print(city)
    cities = City.objects.all()
    return render(request, 'cities/home.html', {'object_list': cities, 'form': form})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = "object"
    template_name = 'cities/detail.html'


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')


class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')