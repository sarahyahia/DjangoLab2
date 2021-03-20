from rest_framework.response import Response
#from django.contrib.auth.models import User, Group
from .serializers import UserSerializer
from  rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated ,BasePermission

@api_view(['POST'])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                    "success":False,
                    "errors":str(e)
            },status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            "success":True,
            "message":"User has been created successfully"
        },status=status.HTTP_201_CREATED)
    return Response(data={
            "success":False,
            "passsword":serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)



# class IsManager(BasePermission):
#     # group = Group(name = "Manager")
#     # #group.save()                    # save this new group for this example
#     # user = User.objects.get(pk = 1) # assuming, there is one initial user 
#     # user.groups.add(group)          # user is now in the "Editor" group
#     def has_permission(self,request, view):
#         return request.user.has_perm("netflix.add_movie")