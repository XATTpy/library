from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    owner = models.ForeignKey('User', related_name='books', on_delete=models.CASCADE)
