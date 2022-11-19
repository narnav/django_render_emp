from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
def index(req):
    return HttpResponse('<h1>about first</h1>')



from .models import Student
from rest_framework import serializers
 
 
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields ='__all__'

@api_view(['GET'])
def data(req):

    products = Student.objects.all()
    serializer = StudentSerializer(products, many=True)
    return Response(serializer.data)

