from rest_framework import serializers
from .models import ImagesModels

class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModels
        fields = ['id', 'image', 'processed_image']
