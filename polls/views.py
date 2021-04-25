from rest_framework import generics
from .serializers import ScoreSerializer
from .models import Score


class ScoreList(generics.ListAPIView):
    '''Score list class is for displaying all the user score'''

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
