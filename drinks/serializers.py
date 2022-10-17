#serializers converts oibjects into data types which is understand by js 
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Drink
    fields = ['id', 'name']
