from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UserList, UserBooks, BookDetail


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/books/', UserBooks.as_view()),
    path('<int:pk>/books/<int:id>/', BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
