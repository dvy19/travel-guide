# urls.py

from django.urls import path
from .views import PlaceCategoryView

urlpatterns = [
    path(
        "categories/create/",
        PlaceCategoryView.as_view(),
        name="category-create"
    ),
]