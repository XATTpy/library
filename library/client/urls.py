from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, UserBooks, BookDetail


urlpatterns = [
    path('', UserList.as_view(), name='users'),
    path('<int:pk>/books/', UserBooks.as_view(), name='books'),
    path('<int:pk>/books/<int:id>/', BookDetail.as_view(), name='book-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
