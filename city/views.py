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

        print("pk:", pk)  # Debugging statement to check the value of pk

        print("Request method:", request.method)  # Debugging statement to check the request method

        print("Request data:", request.data)  # Debugging statement to check the request data

        print("Request query params:", request.query_params)  # Debugging statement to check the query parameters

        print("Request path:", request.path)  # Debugging statement to check the request path


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

        print("Serialized data:", serializer.data)  # Debugging statement to check the serialized data
        print("Serializer errors:", serializer.errors)  # Debugging statement to check for serializer errors

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
