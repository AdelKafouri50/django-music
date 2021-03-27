from rest_framework.response import Response
from netflix.models import Movie
from .serializers import MovieSerializer, UserSerializer
from rest_framework import status, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes




@api_view(['POST'])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
             return Response(data={
                'success': False,
                'message': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={
                'success': True,
                "message": 'User has been created Successfully.'
            }, status=status.HTTP_201_CREATED)
        
        return Response(data={
            'success': False,
            'message': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            'success': True,
            'message': 'Song has been added successfully'
        }, status=status.HTTP_201_CREATED)

    return Response(data={
        'success': False,
        'error': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


@permission_classes([IsAuthenticated,])
class CreateMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer