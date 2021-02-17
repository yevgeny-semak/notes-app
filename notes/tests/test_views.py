import json

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from notes.models import Note, CustomUser
from notes.serializers import NoteSerializer


class GetAllNotesTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test', password='1234', email='test@localhost')
        Note.objects.create(title='test1', content='testcontent1', user=self.user)
        Note.objects.create(title='test2', content='testcontent2', user=self.user)
        Note.objects.create(title='test2', content='testcontent3', user=self.user)

    def test_get_all_notes(self):
        response = self.client.get(reverse('notes'))
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewNoteTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test', password='1234', email='test@localhost')
        self.valid_payload = {
            'title': 'test1',
            'content': 'testcontent1',
            'user': self.user.id
        }
        self.invalid_payload = {
            'title': '',
            'content': 'testcontent1',
            'user': self.user.id
        }

    def test_create_note_with_valid_payload(self):
        response = self.client.post(
            reverse('notes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_note_with_invalid_payload(self):
        response = self.client.post(
            reverse('notes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleNoteTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test', password='1234', email='test@localhost')
        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)

    def test_get_note_with_valid_pk(self):
        response = self.client.get(
            reverse('notes_item', kwargs={'pk': self.note.pk})
        )
        note = Note.objects.get(pk=self.note.pk)
        serializer = NoteSerializer(note)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_with_invalid_pk(self):
        response = self.client.get(
            reverse('notes_item', kwargs={'pk': 10})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateNoteTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test', password='1234', email='test@localhost')
        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)
        self.valid_payload = {
            'title': 'test42',
            'content': 'testcontent42',
            'user': self.user.id
        }
        self.invalid_payload = {
            'title': '',
            'content': 'testcontent43',
            'user': self.user.id
        }

    def test_update_note_with_valid_payload(self):
        response = self.client.put(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note_with_invalid_payload(self):
        response = self.client.put(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleNoteTest(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test', password='1234', email='test@localhost')
        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)

    def test_delete_note_with_valid_pk(self):
        response = self.client.delete(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note_with_invalid_pk(self):
        response = self.client.delete(
            reverse('notes_item', kwargs={'pk': 10}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
