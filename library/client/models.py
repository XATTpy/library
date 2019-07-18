from django.db import models
from django.urls import reverse


class User(models.Model):
    """
    Model representing an user.
    """
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing an book.
    """
    title = models.CharField(max_length=100)
    summary = models.TextField()
    reader = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        return self.title
