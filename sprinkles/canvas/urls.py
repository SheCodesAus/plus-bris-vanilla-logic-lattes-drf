from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('canvas/', views.CanvasList.as_view()),
    path('canvas/<int:pk>/', views.CanvasDetail.as_view()),
    path('sticky_notes/', views.StickyNoteList.as_view()),
    path('sticky_notes/<int:pk>/', views.StickyNoteDetail.as_view()),
    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)