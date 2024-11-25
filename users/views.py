from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Pizza
from users.models import CustomUser, UserPizzaComment


class UserRegistrationAPIView(APIView):

    def post(self, request, *args, **kwargs):
        request_body = request.data
        print('sacbkjsa:', request_body)

        try:
            new_user = CustomUser.objects.create(
                phone_number=request_body['phone_number'],
                first_name=request_body['first_name'],
                last_name=request_body['last_name'],
                password=request_body['password'],
            )
        except IntergrityError:
            return Response(status=400, data={'message': 'sacascas'})

        token, created = Token.objects.get_or_create(user=new_user)
        return Response(
            status=201,
            data={
                'first_name': new_user.first_name,
                'last_name': new_user.last_name,
                'phone_number': new_user.phone_number,
                'token': token.key,
            },
        )


class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        request_body = request.data

        user = CustomUser.objects.get(phone_number=request_body['phone_number'])
        correct = user.check_password(request_body['password'])
        if correct is False:
            return Response(status=400, data={'message': 'вы ввели не правильный пароль'})
        else:
            token, created = Token.objects.get_or_create(user=user)
            return Response(status=200, data={'token': token.key})


class PizzaCommentWriteAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_body = request.data
        current_user = request.user

        try:
            pizza = Pizza.objects.get(id=kwargs['pk'])
        except Pizza.DoesNotExist:
            return Response(status=404, data={'message': 'Такой пиццы не существует'})

        UserPizzaComment.objects.create(
            comment_text=request_body['comment_text'],
            user=current_user,
            pizza=pizza,
        )
        return Response(status=201, data={'message': 'Коментарий успешно добавлен'})


class SayHelloAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        current_user = request.user
        return Response(status=200, data={'message': f'Привет{current_user.first_name}'})
