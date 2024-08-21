from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view())
]