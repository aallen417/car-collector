from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TYPES = (
   ('S', 'Sport'),
   ('L', 'Sedan'),
   ('C', 'Crossover/SUV'),
   ('T', 'Truck')
)

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  type = models.CharField(max_length=1, choices=TYPES, default=TYPES[0][0])
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.model
  
  def get_absolute_url(self):
      return reverse("car-detail", kwargs={"car_id": self.id})
  