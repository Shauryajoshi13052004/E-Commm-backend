from django.urls import path
from .views import (
   AdminCategoryDetailView, AdminCategoryListCreateView, RegisterView, LoginView, 
    UserProfileView, 
    CategoryDetailView,
    CategoryListCreateView,
    ProductListCreateView,
    ProductDetailView,
    CartView,
    OrderView,
    UserOrdersView,
    AdminRegisterView
    
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain access & refresh tokens
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Verify token validity


    # User Endpoints
    # path('users/', UserList.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    # Category Endpoints
    # path('categories/', CategoryList.as_view(), name='category-list'),
    # path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

    # Product Endpoints
    # path('products/', ProductList.as_view(), name='product-list'),
    # path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('admin-register/', AdminRegisterView.as_view(), name='register'),

    path('login/', LoginView.as_view(), name='login'),
    # path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('user/profile/<int:id>/', UserProfileView.as_view(), name='user-profile-by-id'),  # Specific user's profile
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('admin-categories/', AdminCategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('admin-categories/<int:pk>/', AdminCategoryDetailView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/<int:product_id>/', CartView.as_view(), name='cart-delete'),
    path('order/create/', OrderView.as_view(), name='create_order'),
    path('orders/', UserOrdersView.as_view(), name='user_orders'),

]