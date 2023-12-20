from rest_framework import serializers
from app.models import Cafe, Menu, Food

class CafeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'