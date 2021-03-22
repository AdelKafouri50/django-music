from rest_framework.response import Response
from netflix.models import Movie
from .serializers import MovieSerializer
from rest_framework import status, generics
from rest_framework.decorators import api_view




@api_view(['GET',])
def index(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(instance=movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['POST',])
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

class CreateMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer