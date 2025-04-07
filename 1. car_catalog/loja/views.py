from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    return render(request, 'loja/home.html', {'cars': cars})


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'loja/detail.html', {'car': car})