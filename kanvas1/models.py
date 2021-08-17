from django.db import models
from django.db.models.fields import GenericIPAddressField
from django.db.models.query_utils import refs_expression
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
# from django.db.models.




class Activity(models.Model):
    title = models.CharField(max_length=255, unique=True)
    points = models.FloatField()
    submissions = models.ManyToManyField("Submission", related_name="Submission")

class Submission(models.Model):
    grade = models.FloatField(null=True)
    repo = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)




class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User,blank=True)
    

