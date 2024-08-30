import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.
class SumaView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma=int(num_uno) + int (num_dos)
        return Response(suma, status=status.HTTP_200_OK)
    

class RestaView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        resta=int(num_uno) - int (num_dos)
        return Response(resta, status=status.HTTP_200_OK)
    

class MultiplicacionView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        multiplicar=int(num_uno) * int (num_dos)
        return Response(multiplicar, status=status.HTTP_200_OK)
    

class DivisionView(APIView):
    def get(self,request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        try:
            num_uno=int(num_uno)
            num_dos=int(num_dos)
            
            if num_dos == 0:
                return Response("no se puede dividir por 0", status=status.HTTP_400_BAD_REQUEST)
            dividir = num_dos/ num_dos
            return Response(dividir, status=status.HTTP_200_OK)
        except ValueError:
             return Response("deben ser numeros enteros ", status=status.HTTP_400_BAD_REQUEST)
    
    
    