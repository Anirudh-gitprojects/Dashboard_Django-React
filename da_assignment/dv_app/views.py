from django.shortcuts import render
from django.http import request,response,HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DB_Visual
from .serializer import DBSerializer
from rest_framework.renderers import JSONRenderer
import plotly.express as px
from rest_framework import viewsets
# Create your views here.
@api_view(['GET'])
def index(request):
    data=DB_Visual.objects.all()
    serializer=DBSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postFood(request):
    serializer = DBSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

class TodoView(viewsets.ModelViewSet):
    # create a serializer class and
    # assign it to the TodoSerializer class
    serializer_class = DBSerializer
    # define a variable and populate it
    # with the Todo list objects
    queryset = DB_Visual.objects.all()