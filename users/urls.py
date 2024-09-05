from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UserViewSet, UserCreateAPIView, PaymentListAPIView, PaymentCreateAPIView, UserRetrieveAPIView, \
    UserUpdateAPIView, UserDeleteAPIView, UserListAPIView

app_name = UsersConfig.name
router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('payment/',  PaymentListAPIView.as_view(), name='payment_list'),
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    path('users_list/', UserListAPIView.as_view(), name='users_list'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]
urlpatterns += router.urls
