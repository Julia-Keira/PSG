from email.policy import default
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

class Page_header(CMSPlugin):
    title = models.CharField(max_length=9999)
    def __str__(self):
        return self.title

class Iframe(CMSPlugin):
    src = models.CharField(max_length=9999)
    width = models.CharField(max_length=5)
    height = models.CharField(max_length=5)
    def __str__(self):
        return self.src

class Image_one(CMSPlugin):
    picture1 = models.ImageField()
    def __str__(self):
        return ""

class Image_two(CMSPlugin):
    picture1 = models.ImageField()
    picture2 = models.ImageField()
    def __str__(self):
        return ""

class Image_three(CMSPlugin):
    picture1 = models.ImageField()
    picture2 = models.ImageField(default="")
    picture3 = models.ImageField()
    def __str__(self):
        return ""

class Three_mini_windows(CMSPlugin):
    firstText = models.CharField(max_length=300)
    firstImage = models.ImageField()
    secondText = models.CharField(max_length=300)
    secondImage = models.ImageField()
    thirdText = models.CharField(max_length=300)
    thirdImage = models.ImageField()
    def __str__(self):
        return self.firstText

class Two_mini_windows(CMSPlugin):
    firstText = models.CharField(max_length=300)
    firstImage = models.ImageField()
    secondText = models.CharField(max_length=300)
    secondImage = models.ImageField()
    def __str__(self):
        return self.firstText

class One_mini_windows(CMSPlugin):
    firstText = models.CharField(max_length=300)
    firstImage = models.ImageField()
    def __str__(self):
        return self.firstText