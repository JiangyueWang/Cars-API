from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from cars.models import Car
from cars.serializers import CarSerializer
# decorator is going to assign certain permission to the function below


@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serializers = CarSerializer(cars, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializers = CarSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializers = CarSerializer(car)
        return Response(serializers.data)

    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
