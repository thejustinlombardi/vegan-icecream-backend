from rest_framework import serializers
from .models import IceCream


class IceCreamSerializer(serializers.ModelSerializer):
    '''icecream serializer'''

    class Meta:
        '''icecream meta class'''
        model = IceCream
        fields = ('id', 'brand', 'location',
                  'alternatives', 'site', 'photo_url')
