from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Book


class UserTests(APITestCase):
    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('users')
        data = {'name': 'Test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Test')

    def test_get_users(self):
        """
        Ensure we can get a user objects.
        """
        url = reverse('users')
        data = {'name': 'Test'}
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)


class BookTests(APITestCase):
    def test_create_book(self):
        """
        Ensure we can create a new book object and get it.
        """
        url = reverse('users')
        data = {'name': 'Test'}
        self.client.post(url, data, format='json')
        url = reverse('books', args=[1])
        data = {'title': 'Test', 'summary': 'Test', 'user': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test')
        self.assertEqual(Book.objects.get().summary, 'Test')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
