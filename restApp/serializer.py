
# from rest_framework.serializer import ModelSerializer
from rest_framework.serializers import ModelSerializer

from bmpapp.models import Product, Profile

class MySerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
