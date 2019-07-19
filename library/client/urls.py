from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, UserBooks, BookDetail


urlpatterns = [
    path('', UserList.as_view(), name='users'),
    path('<int:pk>/books/', UserBooks.as_view(), name='user_books'),
    path('<int:pk>/books/<int:id>/', BookDetail.as_view(), name='update_book'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
