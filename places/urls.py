# urls.py

from django.urls import path
from .views import PlaceApiView, PlaceCategoryView, PlacesByCityAPIView, ReviewApiView, UserReviewApiView, SavedPlaceApiView, RecommendPlaces, LikePlaceApiView

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
        "my-reviews/",
        UserReviewApiView.as_view(),
        name="user-reviews"
    ),



    path(
        "saved-places/",
        SavedPlaceApiView.as_view(),
        name="saved-places"
    ),


    path(
        "like-place/",
        LikePlaceApiView.as_view(),
        name="like place"
    ),


    path(
        "places/<int:place_id>/",
        PlaceApiView.as_view(),
        name="place-detail"
    ),


    path(
        "places/city/<int:city_id>/", 
        PlacesByCityAPIView.as_view(), 
        name="place-by-city"
        ),

  path(
        "recommend/",
        RecommendPlaces.as_view()
    ),

     path(
        "reviews/",
        ReviewApiView.as_view(),
        name="reviews"
    ),

    # Get single review
    # Update review
    # Partial update review
    # Delete review
    path(
        "reviews/<int:id>/",
        ReviewApiView.as_view(),
        name="review-detail"
    ),
]