from django.urls import path,include
from . import views

#from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('',views.index),
    path('create',views.create),
    path('update/<int:id>',views.update),
    path('delete/<int:pk>',views.DeleteMovie.as_view()),
    path('list/',views.MovieViewSet.as_view({'get': 'list'}))
   # path("login/", obtain_auth_token),
]