from django.db import models
from django import forms
from django.db.models.fields import DateField
from portfolio import settings


class General_info(models.Model):
    image = models.ImageField(upload_to='images/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    summary = models.CharField(max_length=100)
    birth_date = DateField()
    location = models.CharField(max_length=50)

    class Meta():
        verbose_name_plural = "General info"

    def __str__ (self):
        return 'summary'


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=100)
    subheading = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=200)

    def __str__(self):
        model_name = self.heading + ' - ' + self.subheading
        return model_name


class Jobs(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    present_date = models.CharField(max_length=50, default="Present")
    summary = models.CharField(max_length=1000)

    class Meta():
        verbose_name_plural = "Jobs"

    def __str__ (self):
        return self.company_name