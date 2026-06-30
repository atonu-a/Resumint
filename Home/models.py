from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Info(models.Model):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    work_exp =  models.CharField(max_length=255, blank=True, null=True)
    work_exp_details = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    

# Create your models here.
