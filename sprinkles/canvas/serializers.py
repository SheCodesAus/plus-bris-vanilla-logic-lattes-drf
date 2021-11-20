# from django.db import models
from rest_framework import serializers
# from datetime import date
from .models import Canvas, StickyNote

class CanvasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canvas
        fields = [
            'id',
            'team',
            'title',
            'description',
            'is_public',
            'date_created',
            'owner'
            ]

class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyNote
        fields = [
            'title',
            'canvas',
            'who',
            'what',
            'why',
            'anonymous',
            'owner'
            ]
    def create(self,validated_data):
        return StickyNote.objects.create(**validated_data)

