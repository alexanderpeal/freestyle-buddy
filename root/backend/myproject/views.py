from rest_framework import viewsets
from .models import Song
from .serializers import SongSerializer
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

def lyrics_view(request):
    data = {"test": "test message"}
    return JsonResponse(data)

class MyCustomAPIView(APIView):
    def get(self, request, format=None):
        data = {'message': 'Hi from a DRF view!'}
        return Response(data)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def generate_rap_lyrics(request):
    # This is where you'd generate the lyrics. For now, it returns a static line.
    lyrics = "This is just a placeholder for the rap lyrics."
    return Response({"lyrics": lyrics})