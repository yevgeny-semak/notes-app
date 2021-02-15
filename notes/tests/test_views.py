import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from notes.models import Note, User
from notes.serializers import NoteSerializer


class GetNotesTest(APITestCase):

    def setUp(self):
        user = User.objects.create(username='test', password='1234', email='test@localhost')
        Note.objects.create(title='test1', content='testcontent1', user=user)
        Note.objects.create(title='test2', content='testcontent2', user=user)
        Note.objects.create(title='test2', content='testcontent3', user=user)

    def test_get_all_notes(self):
        response = self.client.get(reverse('notes'))
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        self.assertEqual(response.data.pop('notes'), serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
