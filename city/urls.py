
from django.urls import path

from .views import CityView, LoginView, RegisterView

urlpatterns = [

    path("cities/", CityView.as_view()),
    path("cities/<int:pk>/", CityView.as_view()),
    

]