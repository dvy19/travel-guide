
from urllib import request

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from places.models import Place, Review, SavedPlace
from places.serializers import PlaceCategorySerializer, PlaceSerializer, PlaceDetailSerializer, ReviewSerializer, SavedPlaceSerializer


# Create your views here.

class PlaceCategoryView(APIView):

    def post(self,request):

        serializer = PlaceCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Category created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
                            )
        
        return Response(
            {
                "message": "Failed to create category",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

class PlaceApiView(APIView):


    def post(self, request):
        serializer = PlaceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Place created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "message": "Failed to create place",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, request,place_id=None):


        if place_id:
            try:
                place = Place.objects.get(id=place_id)

                serializer = PlaceDetailSerializer(place)

                print("Place data:", serializer.data)  # Debugging statement
                
                return Response(
                    {
                        "message": "Place retrieved successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            except Place.DoesNotExist:
                return Response(
                    {
                        "message": "Place not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(
            {
                "message": "Places retrieved successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


class PlacesByCityAPIView(APIView):

    def get(self, request, city_id):

        search = request.GET.get("search", "")

        places = Place.objects.filter(
            city_id=city_id
        )

        if search:
            places = places.filter(
                name__icontains=search
            )

        serializer = PlaceSerializer(
            places,
            many=True
        )

        return Response({
            "message": "Places retrieved successfully",
            "data": serializer.data
        })
        
class ReviewApiView(APIView):

    def get(self,request,id=None):

        if id:
            try:
                review=Review.objects.get(id=id)
                serializer=ReviewSerializer(review)

                return Response(
                    {
                        "message":"Review retrieved successfully",
                        "data":serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            except Review.DoesNotExist:
                return Response(
                    {
                        "message":"Review not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        
        reviews=Review.objects.all()
        serializer=ReviewSerializer(reviews,many=True)

        return Response(
            {
                "message":"Reviews retrieved successfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    def post(self,request):

        serializer=ReviewSerializer(data=request.data
        )

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "message":"Review created successfully",
                    "data":serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "message":"Failed to create review",
                "errors":serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

    def put(self,request,id):

        try:
            review=Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Response(
                {
                    "message":"Review not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer=ReviewSerializer(review,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Review updated successfully",
                    "data":serializer.data
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                "message":"Failed to update review",
                "errors":serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    

    def patch(self,request,id):

        try:
            review=Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Response(
                {
                    "message":"Review not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer=ReviewSerializer(review,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Review updated successfully",
                    "data":serializer.data
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            {
                "message":"Failed to update review",
                "errors":serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self,request,id):

        try:
            review=Review.objects.get(id=id)
        except Review.DoesNotExist:
            return Response(
                {
                    "message":"Review not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        review.delete()
        return Response(
            {
                "message":"Review deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )

class SavedPlaceApiView(APIView):

    def post(self, request):

        serializer=SavedPlaceSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {
                    "message":"Place saved successfully",
                    "data":serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            {
                "message":"Failed to save place",
                "errors":serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )   
    
    def get(self, request):


        saved_places=SavedPlace.objects.filter(user=request.user)
        serializer=SavedPlaceSerializer(saved_places,many=True)

        return Response(
            {
                "message":"Saved places retrieved successfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    def delete(self, request, id):
        
        try:
            saved_place=SavedPlace.objects.get(id=id,user=request.user)
        except SavedPlace.DoesNotExist:
            return Response(
                {
                    "message":"Saved place not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        saved_place.delete()
        return Response(
            {
                "message":"Saved place deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )


class UserReviewApiView(APIView):

    def get(self, request):
        user_reviews=Review.objects.filter(user=request.user)

        serializer=ReviewSerializer(user_reviews,many=True)

        return Response(
            {
                "message":"User reviews retrieved successfully",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )