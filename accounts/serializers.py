from rest_framework.serializers import ModelSerializer
from .models import * 

class CustomUserSerializer(ModelSerializer):
    
    class Meta:
        model = CustomUser
        exclude = ('last_login', 'password', 'is_admin', 'is_superuser', 'user_permissions', 'groups')