
from django.contrib import admin
from django.urls import path

from products.views import PizzaListAPIView, PizzaDetailAPIView
from users.views import UserRegistrationAPIView, UserLoginAPIView, SayHelloAPIView, PizzaCommentWriteAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/pizzas/', PizzaListAPIView.as_view()),
    path('api/v1/pizzas/<int:pk>/', PizzaDetailAPIView.as_view()),

    path('api/v1/users/registration', UserRegistrationAPIView.as_view()),
    path('api/v1/users/login/', UserLoginAPIView.as_view()),

    path('api/v1/pizzas/<int:pk>/write-comment/', PizzaCommentWriteAPIView.as_view()),

    path('api/v1/say-hello/', SayHelloAPIView.as_view()),
]
