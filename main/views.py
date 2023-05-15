from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
def insertImage(request):
    if request.method == 'POST':
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            image=request.build_absolute_uri(serializer.data['image'])
            return Response({"image":image})
        return Response(serializer.errors)
