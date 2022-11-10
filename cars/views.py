from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car
from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
def cars_list(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many = True)    
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
        
        
@api_view(['GET', "PUT"])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk = pk)
    if request.method == "GET":
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car)
    elif request.method == "PUT":        
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
    return Response(serializer.data)

        
