from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from django.contrib.auth.views import LoginView

# Create your views here.
def about(request):
  return render(request, 'about.html')

@login_required
def car_index(request):
  cars =  Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def car_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', { 'car': car })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    user = form.save()
    login(request, user)
    return redirect('car-index')
  else:
    error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class Home(LoginView):
  template_name = 'home.html'

class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'type', 'description', 'year']
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = ['description']

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'