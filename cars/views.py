from rest_framework.decorators import api_view
from rest_framework.response import Response
from cars.models import Car
from cars.serializers import CarSerializer
# decorator is going to assign certain permission to the function below


@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()
    serializers = CarSerializer(cars, many=True)
    return Response(serializers.data)
