from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, UserBooks, BookDetail


urlpatterns = [
    path('', UserList.as_view(), name='Users'),
    path('<int:pk>/books/', UserBooks.as_view(), name='UserBooks'),
    path('<int:pk>/books/<int:id>/', BookDetail.as_view(), name='UpdateBook'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
