
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path
from . import views

urlpatterns = [

    #path('', views.apiOverview, name='apiOverview'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('product-list/', views.showAll, name='product-list'),
    path('product-detail/<int:pk>/', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/', views.deleteProduct, name='product-delete'),

]
