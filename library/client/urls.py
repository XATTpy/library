from django.urls import path

from .views import UserList, UserBooks


urlpatterns = [
    path('', UserList.as_view(), name='Users'),
    path('<int:pk>/', UserBooks.as_view(), name='UserBooks'),
]
