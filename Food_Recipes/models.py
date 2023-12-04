from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class breakfast_details(models.Model):
    title = models.CharField(max_length=150)
    image= models.ImageField()
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()  
    video = EmbedVideoField()  

    def __str__(self):
        return self.title
    
class dinner_details(models.Model):
    title = models.CharField(max_length=150)
    image= models.ImageField()
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()   
    video = EmbedVideoField() 

    def __str__(self):
        return self.title
    
class juice_details(models.Model):
    title = models.CharField(max_length=150)
    image= models.ImageField()
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()   
    video = EmbedVideoField() 

    def __str__(self):
        return self.title

class sweet_details(models.Model):
    title = models.CharField(max_length=150)
    image= models.ImageField()
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()   
    video = EmbedVideoField() 

    def __str__(self):
        return self.title