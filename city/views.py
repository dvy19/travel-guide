from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from city.models import City
from city.serializers import CitySerializer



# Create your views here.

class CityView(APIView):


    def post(self,request):

        serializer=CitySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "City created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
                )
        
        else:
            return Response(
                {
                    "message": "City creation failed",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self,request,pk):

        try:
            city=City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response(
                {
                    "message": "City not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer=CitySerializer(city,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "City updated successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        
        else:
            return Response(
                {
                    "message": "City update failed",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def get(self, request, pk=None):

        if pk:
            try:
                city = City.objects.get(pk=pk)
            except City.DoesNotExist:
                return Response(
                    {"message": "City not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = CitySerializer(city)

            return Response(
                {
                    "message": "City retrieved successfully",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)

        return Response(
            {
                "message": "Cities retrieved successfully",
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )


'''
python does not support method overloading, so a class can not have two get methods. To handle both single and multiple retrievals, we can use an optional parameter (pk) in the get method. If pk is provided, we retrieve a single city; if not, we retrieve all cities.
'''
