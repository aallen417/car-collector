from django.db import models

# Create your models here.
class Car(models.Model):
  make = models.CharField(max_length=25)
  model = models.CharField(max_length=25)
  description = models.TextField(max_length=250)
  year = models.IntegerField()

  def __str__(self):
      return self.model