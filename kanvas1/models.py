from django.db import models
from django.db.models.fields import GenericIPAddressField
from django.db.models.query_utils import refs_expression

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Submission(models.Model):
    grade = models.FloatField()
    repo = models.CharField(max_length=255)
    user_id = models.ManyToManyField(User)
    activity_id = models.ManyToManyField(Activity)

class Activity(models.Model):
    title = models.CharField(max_length=255, unique=True)
    points = models.FloatField()
    submission = models.ManyToManyField(Submission)

class Course(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)


# class User_course(models.Model):
#     user_id = models.ManyToManyField(User)
#     course_id = models.ManyToManyField(Course)