from django.db import models

#from django.contrib import auth

class Home(models.Model):
    event_description=models.CharField(max_length=255)
    event_pic=models.ImageField(null=True,blank=True,upload_to="media/")

    class Meta:
        ordering=['-id']

class Home_features(models.Model):
    title1=models.CharField(max_length=255,null=True,blank=True)
    photo1=models.ImageField(null=True,blank=True,upload_to="media/")

    title2=models.CharField(max_length=255,null=True,blank=True)
    photo2=models.ImageField(null=True,blank=True,upload_to="media/")

    title3=models.CharField(max_length=255,null=True,blank=True)
    photo3=models.ImageField(null=True,blank=True,upload_to="media/")

    title4=models.CharField(max_length=255,null=True,blank=True)
    photo4=models.ImageField(null=True,blank=True,upload_to="media/")

class Home_facility(models.Model):
    pic1=models.ImageField(null=True,blank=True,upload_to="media/")
    pic2=models.ImageField(null=True,blank=True,upload_to="media/")
    pic3=models.ImageField(null=True,blank=True,upload_to="media/")
    pic4=models.ImageField(null=True,blank=True,upload_to="media/")

class About(models.Model):
    vision_pic=models.ImageField(null=True,blank=True,upload_to="media/")
    making_pic=models.ImageField(null=True,blank=True,upload_to="media/")
    sidebar_pic=models.ImageField(null=True,blank=True,upload_to="media/")

class Studentlife(models.Model):
    description=models.CharField(max_length=255)
    pics=models.ImageField(upload_to="media/")
    
    class Meta:
        ordering=['-id']
        # ordering=['-description']