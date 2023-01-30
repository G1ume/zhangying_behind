# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=16)
    name = models.TextField(max_length=16)
    avatar = models.ImageField(null=True)


class Chapter(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    top = models.CharField(max_length=16)
    name = models.TextField(max_length=16)
    user = models.CharField(max_length=16)


class Question(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    name = models.TextField(max_length=16)
    user = models.CharField(max_length=16)
    chapter = models.CharField(max_length=16)
    question_description = models.TextField(max_length=128, null=True)
    answer_description = models.TextField(max_length=128, null=True)
    img_question = models.ImageField(null=True)
    img_answer = models.ImageField(null=True)
