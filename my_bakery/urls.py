from django.urls import path,re_path
from .import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView




urlpatterns = [
    path('ingredients/',views.IngredientListView.as_view()),
    path('ingredients-Details-items/', views.IngredientDetailView.as_view()),
    path('inventory/', views.InventoryListView.as_view()),
    path('inventory-detail/',views.InventoryDetailView.as_view()),
    path('orders/', views.OrderListView.as_view()),
    path('orderDetail/',views.OrderDetailView.as_view()),
    # path('register/',views.RegisterView.as_view()),
    # path('login/',views.LoginView.as_view()),
    path('product-search/',views.ProductSearchView.as_view()),
    path('add_to-basket/',views.AddToBasketView.as_view()),
    path('place-order/',views.PlaceOrderView.as_view()),
    path('',views.HomeView.as_view()),
    #path('admin/',views.AdminDashboardView.as_view()),
    path('baking/',views.BakeryItemListView.as_view()),
    path('bakitems/',views.BakeryItemDetailView.as_view()),
    path('token/', views.CustomTokenObtainPairView.as_view()),
    path('token/refresh/', views.TokenRefreshView.as_view()),
    



]

urlpatterns=format_suffix_patterns(urlpatterns)