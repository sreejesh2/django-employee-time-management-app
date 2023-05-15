from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router=DefaultRouter()

router.register('user',views.UserCreationView,basename='users'),

urlpatterns = [
    path('token/',TokenObtainPairView.as_view(),name='obtain_pairview'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('user/login/', views.UserLoginView.as_view(), name='user_login'),


]+router.urls
