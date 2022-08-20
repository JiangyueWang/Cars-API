from rest_framework.decorators import api_view
from rest_framework.response import Response
# decorator is going to assign certain permission to the function below


@api_view(['GET'])
def cars_list(request):
    return Response('ok!')
