from django.urls import path
from . import views

urlpatterns = [    
    path('',views.index, name='index'),
    path('create',views.create,name="create"),
    path('display/<int:id>',views.display,name="display"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
  #  path("<str:name>", views.hello , name="hello"),
]
