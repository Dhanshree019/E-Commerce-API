from django.db import transaction
from rest_framework.views import APIView,status
from rest_framework.response import Response
from accounts.models import CustomUser
from orders.serializers import *
from orders.models import *
# Create your views here.

class OrderView(APIView):
    @transaction.atomic
    def post(self,request):
        try:
            rd = request.data
            rd['user'] = CustomUser.objects.filter(id=rd['user']).first()
            order_data =  Order.objects.create(**rd)
            if order_data:
                order_data = OrderSerializer(order_data).data
                return Response({"success":True,"message":"Order created successfully","data":order_data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Provide proper data"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @transaction.atomic           
    def get(self,request):
        try:
            order_data = Order.objects.all()
            if order_data:
                order_data = OrderSerializer(order_data,many=True).data
                return Response({"success":True,"message":"Order data reterived successfully","data":order_data}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class GetOrderView(APIView):
    @transaction.atomic           
    def get(self,request,id):
        try:
            order_data = Order.objects.filter(id=id)
            if order_data:
                order_data = OrderSerializer(order_data,many=True).data
                return Response({"success":True,"message":"Order data reterived successfully","data":order_data}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @transaction.atomic
    def put(self,request,id):
        try:
            order_data = Order.objects.filter(id=id).first()
            if order_data:
                order_data = OrderSerializer(instance=order_data,data=request.data,partial=True)
                if order_data.is_valid():
                    order_data.save()
                    return Response({"success":True,"message":"Order updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     