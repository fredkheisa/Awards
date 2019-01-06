from django.contrib.auth.models import User
import datetime as dt
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import numpy as np



class Profile(models.Model):

    profile_pic = models.ImageField(upload_to = 'images/', blank=True)
    bio = models.TextField()
    contact = models.CharField(max_length = 30, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)

   

    def __str__(self):
                return self.bio

class Project(models.Model):
    """
    Class that contains Project details
    """
    title = models.CharField(max_length = 20)
    landing_page = models.ImageField(upload_to = 'images/')
    description = models.TextField()
    link = models.URLField(max_length = 100)
    rating = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

    def __str__(self):
                return self.title

class DesignRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Project)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class ContentRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Project)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class UsabilityRating(models.Model):
   RATING_CHOICES = (
       (1, '1'),
       (2, '2'),
       (3, '3'),
       (4, '4'),
       (5, '5'),
       (6, '6'),
       (7, '7'),
       (8, '8'),
       (9, '9'),
       (10, '10')
   )
   project = models.ForeignKey(Project)
   pub_date = models.DateTimeField(auto_now=True)
   profile = models.ForeignKey(Profile)
   rating = models.IntegerField(choices=RATING_CHOICES, default=0)

