from pyexpat import model
from turtle import title
from cms.models.pluginmodel import CMSPlugin

from django.db import models

class Main_page_window_model(CMSPlugin):
    title = models.CharField(max_length= 200)
    description = models.CharField(max_length=200)
    picture = models.ImageField()
    link = models.CharField(max_length=500)
    def __str__(self):
        return self.title

class Resolution_model(CMSPlugin):
    title = models.CharField(max_length=9999)
    description = models.TextField()
    resolution = models.FileField()
    date = models.DateField()
    def __str__(self):
        return self.title