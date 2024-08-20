from django.contrib.auth.models import auth 
from django.db import transaction

from rest_framework.views import APIView , status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import *
from .serializers import *

# Create your views here.

class LoginView(APIView):
    permission_classes =[]
    authentication_classes = []
    
    @transaction.atomic
    def post(self,request):
        try:
            rd = request.data
            print("data :", rd)
            is_new_user = False
            user = auth.authenticate(email=rd['email'],password=rd['password'])
            print("user :",user)
            if user == None:
                if CustomUser.objects.filter(email=rd['email']).exists():
                    return Response({"success": True, "message": "Credentials does not macthed!"})
                user = CustomUser.objects.create_user(password=rd['password'], name=rd['name'], email=rd['email'])
                is_new_user = True
            
            token = RefreshToken.for_user(user)
            data = CustomUserSerializer(user).data

            return Response({"success": True, "message": "Login successful !", "data": data,
                            "is_new_user": is_new_user,
                            "authToken": {
                                'type': 'Bearer',
                                'access': str(token.access_token),
                                'refresh': str(token),
                            }}, status=status.HTTP_201_CREATED if is_new_user else status.HTTP_200_OK)


        except Exception as err:
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
  

    @transaction.atomic
    def post(self,request):
        try:
            refresh_token = request.data.get("refresh_token")

            if not refresh_token:
                return Response({"success": False, "message": "Refresh token is required."},
                                status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success":True,"message":"Logout sucessfully !"},status=status.HTTP_200_OK)

        except Exception as err :
            print("Error :",err)
            return Response({"success":False,"message":"Unexpected error occurred!"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



