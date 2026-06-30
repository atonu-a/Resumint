from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    
    
    def __str__(self):
        return self.full_name


class Experience(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="experiences"
    )
    company = models.CharField(max_length=255)
    time_line = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    description = models.TextField()
    
    
class Skill(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)
    
    
class Education(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    institute = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    

# Create your models here.
