from django.db import models
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    # file = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)
@receiver(post_save, sender=Car)
def cal_car_api(sender, instance, **kwargs):
    print ('Car object created or updated')
    print (sender, instance, kwargs)