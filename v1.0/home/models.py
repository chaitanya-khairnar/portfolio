from django.db import models
from django.db.models.fields import NullBooleanField

class About(models.Model):
    portfolio_image = models.ImageField(upload_to='media/', null=True)
    name = models.CharField(max_length=25, default='chk')
    address = models.CharField(max_length=100, null=True)
    contact_number_ext = models.CharField(max_length=3, null=True)
    contact_number = models.CharField(max_length=9, null=True)
    contact_email = models.CharField(max_length=100, null=True)
    summary = models.TextField(max_length=800, null=True)
    
class Experience(models.Model):
    company_icon = models.ImageField(upload_to='media/', null=True)
    position = models.CharField(max_length=50, null=True)
    company_name = models.CharField(max_length=50, default='chk')
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    responsibilities = models.TextField(null=True)

class Skills(models.Model):
    skill_image = models.ImageField(upload_to='media/', null=True)
