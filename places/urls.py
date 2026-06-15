# urls.py

from django.urls import path
from .views import PlaceApiView, PlaceCategoryView

urlpatterns = [
    path(
        "categories/create/",
        PlaceCategoryView.as_view(),
        name="category-create"
    ),

      path(
        "places/",
        PlaceApiView.as_view(),
        name="place-list"
    ),

    path(
        "places/<int:place_id>/",
        PlaceApiView.as_view(),
        name="place-detail"
    ),
]