from django.shortcuts import render
from django.http import HttpResponse

class Car:
  def __init__(self, make, model, description, year):
    self.make = make
    self.model = model
    self.description = description
    self.year = year

cars = [
  Car('BMW', 'M3', 'S58 powered ', 2024),
  Car('Tesla', 'Model 3', 'Electric', 2024),
  Car('Mercedes', 'C63', 'Electrified 4 cyl powered', 2024),
  Car('Audi', 'RS4', 'Turbo V6 powered', 2024),
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def car_index(request):
  return render(request, 'cars/index.html', { 'cars': cars })