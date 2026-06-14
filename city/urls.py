
from django.urls import path

from .views import CityView

urlpatterns = [

    path("cities/", CityView.as_view()),
    path("cities/<int:pk>/", CityView.as_view()),
    
]