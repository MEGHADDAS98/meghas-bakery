# serializers.py
from rest_framework import serializers
from .models import Ingredient, BakeryItem, Inventory, Order, CustomUser
# from rest_framework.authtoken.serializers import UserSerializer


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class BakeryItemSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=True)

    class Meta:
        model = BakeryItem
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    item = BakeryItemSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = BakeryItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255)