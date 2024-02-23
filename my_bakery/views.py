# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Ingredient, BakeryItem, Inventory, Order, CustomUser,Basket,LineItem,OrderItem,BasketItem
from .serializers import IngredientSerializer, BakeryItemSerializer, InventorySerializer, OrderSerializer, UserSerializer, TokenSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            user.save()
        data = super().validate(attrs)
        user = self.user
        data['user_id'] = user.id
        data['email'] = user.email
        data['username'] = user.username
        return data
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class HomeView(APIView):
    def get(self, request):
        return HttpResponse("Welcome to my MEGHA'S BAKERY!")


class IngredientListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IngredientDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return Ingredient.objects.get(pk=pk)
        except Ingredient.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data)

    def put(self, request, pk):
        ingredient = self.get_object(pk)
        serializer = IngredientSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ingredient = self.get_object(pk)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BakeryItemListView(APIView):
    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        bakery_items = BakeryItem.objects.all()
        serializer = BakeryItemSerializer(bakery_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BakeryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BakeryItemDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return BakeryItem.objects.get(pk=pk)
        except BakeryItem.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        bakery_item = self.get_object(pk)
        serializer = BakeryItemSerializer(bakery_item)
        return Response(serializer.data)

    def put(self, request, pk):
        bakery_item = self.get_object(pk)
        serializer = BakeryItemSerializer(bakery_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bakery_item = self.get_object(pk)
        bakery_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class InventoryListView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InventoryDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, pk):
        inventory = self.get_object(pk)
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inventory = self.get_object(pk)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk, user=self.request.user)
        except Order.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key, "user_id": user.id, "email": user.email, "username": user.username}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user is None:
#             return Response({"detail": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key, "user_id": user.id, "email": user.email, "username": user.username}, status=status.HTTP_200_OK)
    

class ProductSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        q = request.GET.get('q', '')
        products = BakeryItem.objects.filter(Q(name__icontains=q)|Q(description__icontains=q))[:10]
        serializer = BakeryItemSerializer(products, many=True)
        return Response(serializer.data)
    
    def place_order(request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        order = Order.objects.create(user=request.user, total_amount=sum([line_item.quantity*line_item.product.cost_price for line_item in basket.lines.all()]))
        for line_item in basket.lines.all():
            order_item = OrderItem.objects.create(order=order, product=line_item.product, quantity=line_item.quantity, cost_price=line_item.product.cost_price, selling_price=line_item.product.selling_price)
        basket.clear()
        return JsonResponse({"success": True})
    
class AddToBasketView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        item_id = request.data.get('id')
        quantity = request.data.get('quantity', 1)

        try:
            item = BakeryItem.objects.get(id=item_id)
        except BakeryItem.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

        basket, created = Basket.objects.get_or_create(user=request.user)

        basket_item, created = BasketItem.objects.get_or_create(basket=basket, item=item)
        basket_item.quantity += quantity
        basket_item.save()

        return Response({'success': 'Item added to basket'})
class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        basket = Basket.objects.filter(user=request.user).first()

        if not basket:
            return Response({'error': 'Basket is empty'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user, total_amount=0, status='pending', date_ordered=timezone.now())

        total_amount = 0

        for basket_item in basket.items.all():
            order_item = OrderItem.objects.create(order=order, product=basket_item.item, quantity=basket_item.quantity, cost_price=basket_item.item.cost_price, selling_price=basket_item.item.selling_price)
            total_amount += order_item.selling_price * order_item.quantity

        order.total_amount = total_amount
        order.save()

        basket.items.clear()

        return Response({'total_amount': total_amount})
    