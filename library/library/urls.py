from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('client.urls')),
    path('', RedirectView.as_view(url='/users/', permanent=True)),
]
