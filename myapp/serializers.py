from rest_framework import serializers
from .models import Category, Banner

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'

class BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'