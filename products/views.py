from django.db import transaction

from rest_framework.response import Response 
from rest_framework.views import APIView, status

from products.models import *
from products.serializers import *

# Create your views here.

class ProductCategoryView(APIView):
    
    @transaction.atomic
    def post(self,request):
        try:
            rd = request.data
            product_category = ProductCategory.objects.create(**rd)
            if product_category:
                product_category = ProductCategorySerializer(product_category).data
                return Response({"success":True,"message":"Product Category created successfully","data":product_category}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Provide proper data"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,request):
        try:
            all_categories = ProductCategory.objects.all()
            if all_categories is not None:
                all_categories = ProductCategorySerializer(all_categories, many=True).data
                return Response({"success":True,"message":"Product categories reterived successfully","data":all_categories}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)
 
        
        except Exception as err:
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



class ProductView(APIView):
    
    @transaction.atomic
    def post(self,request):
        try:
            rd = request.data
            rd['category'] =  ProductCategory.objects.filter(id=rd['category']).first()
            product = Product.objects.create(**rd)
            if product:
                product = ProductSerializer(product).data
                return Response({"success":True,"message":"Product created successfully","data":product}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Provide proper data"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class GetProductView(APIView):
    
    @transaction.atomic
    def get(self,request,id):
        try:
            # product_id = request.GET.get('product_id')
            product_data = Product.objects.filter(id=id).first()
            if product_data:
                product_data = ProductSerializer(product_data).data
                return Response({"success":True,"message":"Product retrived successfully","data":product_data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


        
    