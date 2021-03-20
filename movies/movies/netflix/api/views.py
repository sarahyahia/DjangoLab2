from rest_framework.response import Response
from netflix.models import Movie
from .serializers import MovieSerializer
from  rest_framework import status, generics,viewsets 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
#from ./users/views import IsManger


@api_view(["Get",])
@permission_classes([IsAuthenticated,]) #IsManager
def index(request):
    movies = Movie.objects.all()
    serialzier = MovieSerializer(instance=movies,many=True)
    return Response(data=serialzier.data, status=status.HTTP_200_OK)


@api_view(["POST",])
@permission_classes([IsAuthenticated,IsAdminUser])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Movie has been created successfuly"
        },status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)




@api_view(["POST","PUT"])
@permission_classes([IsAuthenticated,IsAdminUser])
def update(request,id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(data=request.data,instance=movie)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Movie has been updated successfully"
        },status=status.HTTP_202_ACCEPTED)
    
    return Response(data={
        "success": False,
        "errors": serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)


class DeleteMovie(generics.DestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]