from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getdata(request):
    stdata=Studinfo.objects.all()
    serial=StudSerial(stdata,many=True)
    return Response(data=serial.data)


@api_view(['GET'])
def searchdata(request,id):
    try:
        stid=Studinfo.objects.get(id=id)
    except Studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=StudSerial(stid)
    return Response(data=serial.data)


@api_view(['DELETE','GET'])
def deletedata(request,id):
    try:
        stid=Studinfo.objects.get(id=id)
    except Studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=StudSerial(stid)
        return Response(data=serial.data)
    if request.method=='DELETE':
        Studinfo.delete(stid)
        return Response(status=status.HTTP_202_ACCEPTED)
        
    