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

from dotenv import load_dotenv
import os

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")

# @api_view(['GET'])
# def generate_rap_lyrics(request):
#     # This is where you'd generate the lyrics. For now, it returns a static line.
#     lyrics = "This is just a placeholder for the rap lyrics."
#     return Response({"lyrics": lyrics})

import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def generate_rap_lyrics(request):
    # Load the API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    # Get a seed or topic from the request if provided
    topic = request.query_params.get('topic', 'freestyle rap')

    try:
        # Call the OpenAI API to generate rap lyrics
        response = openai.Completion.create(
            engine="text-davinci-003", # You might need to adjust the engine based on availability and capability
            prompt=f"Write a short verse for a rap song about {topic}.",
            temperature=0.7,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        lyrics = response.choices[0].text.strip()
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    return Response({"lyrics": lyrics})
