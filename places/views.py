
from urllib import request

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from places.models import Place, Review
from places.serializers import PlaceCategorySerializer, PlaceSerializer, PlaceDetailSerializer, ReviewSerializer


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
            serializer.save()
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
