from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Pizza
from products.serializers import PizzaSerializer, PizzaDetailSerializer


class PizzaListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print('oookk')
        pizza_list = Pizza.objects.all()
        serializers = PizzaSerializer(instance=pizza_list, many=True)
        response_body = serializers.data
        return Response(status=200, data=response_body)


class PizzaDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            pizza = Pizza.objects.get(id=kwargs['pk'])
        except Pizza.DoesNotExist:
            return Response(status=404, data={'message': 'Такой пиццы не сушествует'})
        serializer = PizzaDetailSerializer(instance=pizza, many=False)
        response_body = serializer.data
        return Response(status=200, data=response_body)
