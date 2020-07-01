from .serialization import serializationClass
from .models import subModel
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models_insert import createSubModel
from .serialization import createSubSerialize
from rest_framework import status

@api_view(['GET'])
def showSub(request):
    if request.method == 'GET' :
        results = subModel.objects.all()
        serialize = serializationClass(results, many = True)
        return Response(serialize.data)

@api_view(['POST'])
def saveSub(request):
    if request.method == 'POST':
        saveSerialize = createSubSerialize(data=request.data)
        if saveSerialize.is_valid():
            saveSerialize.save()
            return Response(saveSerialize.data, status = status.HTTP_201_CREATED)
            return Response(saveSerialize.data, status = status.HTTP_400_BAD_REQUEST)
