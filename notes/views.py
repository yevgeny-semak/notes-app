from rest_framework.response import Response
from rest_framework.views import APIView

from notes.models import Note
from notes.serializers import NoteSerializer


class NotesView(APIView):

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        notes = serializer.data
        return Response({'notes': notes, })


class NotesItemView(APIView):
    pass
