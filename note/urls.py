from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note-list'),
    path('detail/<int:pk>/', views.note_detail, name='note-detail'),
    path('create/', views.note_create, name='note-create'),
    path('update/<int:pk>/', views.note_update, name='note-update'),
    path('delete/<int:pk>/', views.note_delete, name='note-delete'),
]
