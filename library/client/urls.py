from django.urls import path

from .views import UserView


app_name = "users"

urlpatterns = [
    path('users/', UserView.as_view({'get': 'list'})),
    path('users/<int:pk>', UserView.as_view({'get': 'retrieve'})),
]