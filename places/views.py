
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from places.models import Place
from places.serializers import PlaceCategorySerializer, PlaceSerializer, PlaceDetailSerializer


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
    
        
        
