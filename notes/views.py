from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from notes.models import Note
from notes.serializers import NoteSerializer


class NotesView(APIView):

    def get(self, request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        notes = serializer.data
        return Response({'notes': notes, })

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'user': request.data.get('user'),
        }
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotesItemView(APIView):
    pass
