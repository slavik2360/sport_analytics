from django.urls import path

# Local
from .views import MainView


urlpatterns = [
    path('', MainView.as_view())
]
