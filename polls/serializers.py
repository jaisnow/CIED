from rest_framework import serializers
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Score
        fields = ['user_id', 'exam_id', 'score']
