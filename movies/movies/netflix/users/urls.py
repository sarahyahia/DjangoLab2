from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup',views.api_signup),
    path("login/", obtain_auth_token),
    
]
