from django.db import models
from django.urls import reverse


class User(models.Model):
    """
    Model representing an user.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing an book.
    """
    title = models.CharField(max_length=100)
    summary = models.TextField()
    user = models.ForeignKey('User', related_name='books', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
