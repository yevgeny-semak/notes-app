from django.urls import path

from notes.views import NotesView, NotesItemView


urlpatterns = [
    path('notes/', NotesView.as_view(), name='notes'),
    path('notes/<int:pk>', NotesItemView.as_view(), name='notes_item')
]