from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_auth.views import LoginView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models

class ItemListViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer

class CatogoryItemListView(APIView):
    def get(self,request,catogory):
        items = models.Item.objects.filter(catogory = catogory)
        serializer = serializers.ItemSerializer(items,many = True)
        return Response(serializer.data)

class OrderViewSet(viewsets.ViewSet):
    def list(self,request):
        orders = models.Order.objects.all()
        serializer = serializers.OrderSerializer(orders,many = True)
        return Response(serializer.data)
    
    def create(self,request):
        order,created = models.Order.objects.get_or_create(finised = False)
        item_datas = request.data
        for item_data in item_datas:
            item = models.Item.objects.get(name = item_data['name'], id = item_data['id'])
            # print(item_data['quantity'])
            order_item = models.OrderItem.objects.create(order = order, item = item, quantity = item_data['quantity'])
        order.finised = True
        order.save()
        # print(data)
        return Response(serializers.OrderSerializer(order).data)

    def retrieve(self,request,pk):
        order = models.Order.objects.get(pk = pk)
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data)

# class CustomLoginView(LoginView):
#     def get_response(self):
#         orginal_response = super().get_response()
#         token_data = orginal_response.data['key']
#         token = Token.objects.get(key = token_data)
#         user = token.user
#         extra_data = {'username' : user.username, 'email' : user.email}
#         orginal_response.data.update(extra_data)
#         return orginal_response