# from django.http import JsonResponse
from rest_framework import generics
# Create your views here.
from .models import IceCream
# Import serializers
from .serializers import IceCreamSerializer


class IceCreamList (generics.ListCreateAPIView):
    '''list create'''
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class IceCreamDetail (generics.RetrieveUpdateDestroyAPIView):
    '''IceCream CRUD'''
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer
