from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from . import currencyRequest

# Create your views here.
class apiOverview(APIView):
    def get(self, request):
        return Response("API Base Points")

class conversion(APIView):
    def get(self, request):
        result = currencyRequest.conversion("USD", "EUR", 100)
        return Response(result)