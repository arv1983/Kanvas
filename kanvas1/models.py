from django.db import models
from django.db.models.fields import GenericIPAddressField
from django.db.models.query_utils import refs_expression

# class User(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(ma)
#     is_staff
#     is_superuser

# class Submission(models.Model):
#     grade
#     repo
#     user_id
#     activity_id

# class Activity(models.Model):
#     title
#     points
#     submission

# class User_course(models.Model):
#     user_id
#     course_id

# class Course(models.Model):
#     name 
#     users