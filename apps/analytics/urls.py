from django.urls import path
from .views import MainView, ToggleFavoriteView

urlpatterns = [
    path('', MainView.as_view()),
    path('toggle_favorite/<int:match_id>/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
