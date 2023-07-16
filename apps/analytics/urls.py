from django.urls import path

# Local
from .views import index


urlpatterns = [
    path('', index)
]
