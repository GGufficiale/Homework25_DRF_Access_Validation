from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Payment, User
from users.serializer import PaymentSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    """Опция создания нового юзера"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    """Настройка для разрешения создавать нового юзера всем"""
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_lesson', 'paid_course', 'payment_method']
    ordering_fields = ['-date_of_payment']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
