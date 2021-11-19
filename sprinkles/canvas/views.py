from django.shortcuts import render

from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Canvas, StickyNote
from .serializers import CanvasSerializer, StickyNoteSerializer
from .permissions import IsOwnerOrReadOnly

class CanvasList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        ]

    def get(self, request):
        canvas = Canvas.objects.all()
        serializer = CanvasSerializer(canvas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CanvasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class CanvasDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            canvas =Canvas.objects.get(pk=pk)
            self.check_object_permissions(self.request,canvas)
            return canvas
        except Canvas.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        canvas = self.get_object(pk)
        serializer = CanvasSerializer(canvas)
        return Response(serializer.data)
    
    def put(self, request, pk):
        canvas = self.get_object(pk)
        data = request.data
        serializer = CanvasSerializer(
            instance=canvas,
            data=data,partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        canvas = self.get_object(pk)
        canvas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StickyNoteList(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get(self, request):
        sticky_notes = StickyNote.objects.all()
        serializer = StickyNoteSerializer(sticky_notes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StickyNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class StickyNoteDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]
        
    def get_object(self, pk):
        try:
            sticky_note =StickyNote.objects.get(pk=pk)
            self.check_object_permissions(self.request,sticky_note)
            return sticky_note
        except StickyNote.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sticky_note = self.get_object(pk)
        serializer = StickyNoteSerializer(sticky_note)
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = StickyNoteSerializer(
            instance=pledge,
            data=data,partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        sticky_note = self.get_object(pk)
        sticky_note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
