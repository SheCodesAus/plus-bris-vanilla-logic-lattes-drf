from rest_framework import serializers
from .models import Canvas, StickyNote

# class CanvasSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     team = serializers.CharField(max_length=200)
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=None)
#     is_public = serializers.BooleanField()
#     date_created = serializers.ReadOnlyField()
#     user = serializers.ReadOnlyField(source='user.id')
    
    
#     def create(self, validated_data):
#         return StickyNote.objects.create(**validated_data)

# class StickyNoteSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     title = serializers.CharField(max_length=200)
#     who = serializers.CharField(max_length=200)
#     what = serializers.CharField(max_length=200)
#     why = serializers.CharField(max_length=200)
#     anonymous = serializers.BooleanField()
#     user = serializers.ReadOnlyField(source='user.id')

#     def create(self, validated_data):
#         return Canvas.objects.create(**validated_data)

# class CanvasDetailSerializer(CanvasSerializer):
#     sticky_notes = StickyNoteSerializer(many=True, read_only=True)

#     def update(self, instance, validated_data):
#         instance.team = validated_data.get('team',instance.team)
#         instance.title = validated_data.get('title',instance.title)
#         instance.description = validated_data.get('description',instance.description)
#         instance.is_public = validated_data.get('is_public',instance.is_public)
#         instance.date_created = validated_data.get('date_created',instance.date_created)
#         instance.user = validated_data.get('user',instance.user)
#         instance.save()   
#         return instance

# class StickyNoteDetailSerializer(StickyNoteSerializer):
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.who = validated_data.get('who',instance.who)
#         instance.what = validated_data.get('what',instance.what)
#         instance.why = validated_data.get('why',instance.why)
#         instance.anonymous = validated_data.get('anonymous',instance.anonymous)
#         instance.user = validated_data.get('user',instance.user)

#         return instance



class CanvasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canvas
        fields = [
            'id',
            'title',
            'description',
            'is_public',
            'date_created',
            'user'
            ]

class StickyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickyNote
        fields = [
            'id',
            'project',
            'who',
            'what',
            'why',
            'user'
            ]
