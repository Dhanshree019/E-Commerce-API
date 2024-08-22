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
                return Response({"success":True,"message":"Product categories reterived successfully","data":all_categories}, status=status.HTTP_200_OK)
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
        
    def get(self,request):
        try:
            all_products = Product.objects.all()
            if all_products is not None:
                all_products = ProductSerializer(all_products, many=True).data
                return Response({"success":True,"message":"Products reterived successfully","data":all_products}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)
 
        
        except Exception as err:
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
                return Response({"success":True,"message":"Product retrived successfully","data":product_data}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    @transaction.atomic
    def put(self,request,id):
        try:
            # product_id = request.GET.get('product_id')
            product_data = Product.objects.filter(id=id).first()
            if product_data:
                product_data = ProductSerializer(instance=product_data,data=request.data,partial=True)
                if product_data.is_valid():
                    product_data.save()
                    return Response({"success":True,"message":"Product updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @transaction.atomic
    def delete(self,request,id):
        try:
            # product_id = request.GET.get('product_id')
            product_data = Product.objects.filter(id=id)
            if product_data:
                if product_data.exists():
                    product_data.delete()
                    return Response({"success":True,"message":"Product deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ProductReviewView(APIView):

    @transaction.atomic
    def post(self,request,id):
        try:
            rd = request.data
            rd['product'] = Product.objects.filter(id=id).first()
            rd['user'] = CustomUser.objects.filter(id=rd['user']).first()
            product_review =  ProductReview.objects.create(**rd)
            if product_review:
                product_review = ProductReviewSerializer(product_review).data
                return Response({"success":True,"message":"Product review created successfully","data":product_review}, status=status.HTTP_201_CREATED)
            else:
                return Response({"success":False,"message":"Provide proper data"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @transaction.atomic           
    def get(self,request,id):
        try:
            review_data = ProductReview.objects.filter(product=id)
            if review_data:
                review_data = ProductReviewSerializer(review_data,many=True).data
                return Response({"success":True,"message":"Product review reterived successfully","data":review_data}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                

class UpadteProductReviewView(APIView):
    @transaction.atomic
    def put(self,request,id):
        try:
            review_data = ProductReview.objects.filter(id=id).first()
            if review_data is not None:
                review_data = ProductReviewSerializer(instance=review_data,data=request.data,partial=True)
                if review_data.is_valid():
                    review_data.save()
                    return Response({"success":True,"message":"Product review updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @transaction.atomic
    def delete(self,request,id):
        try:
            review_data = ProductReview.objects.filter(id=id)
            if review_data:
                if review_data.exists():
                    review_data.delete()
                    return Response({"success":True,"message":"Product review deleted successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"success":False,"message":"Data not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     