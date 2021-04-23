import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser

from notes.models import Note
from notes.serializers import NoteSerializer


def set_up_user_with_access_token(obj):
    user = CustomUser.objects.create_user(username='test', password='1234', email='test@localhost')

    token_access = obj.client.post(
        reverse('token_obtain'),
        data=json.dumps({'email': 'test@localhost', 'password': '1234'}),
        content_type='application/json'
    ).data.pop('access')

    return user, token_access


class GetUserNotesTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        Note.objects.create(title='test1', content='testcontent1', user=self.user)
        Note.objects.create(title='test2', content='testcontent2', user=self.user)
        Note.objects.create(title='test2', content='testcontent3', user=self.user)

    def test_get_all_notes(self):
        response = self.client.get(
            reverse('notes'),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        notes = Note.objects.filter(user=self.user.id)
        serializer = NoteSerializer(notes, many=True)
        self.assertEqual(response.data, {'notes': serializer.data})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateNewNoteTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        self.valid_payload = {
            'title': 'test1',
            'content': 'testcontent1'
        }
        self.invalid_payload = {
            'title': '',
            'content': 'testcontent1'
        }

    def test_create_note_with_valid_payload(self):
        response = self.client.post(
            reverse('notes'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_note_with_invalid_payload(self):
        response = self.client.post(
            reverse('notes'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetSingleNoteTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)

    def test_get_note_with_valid_pk(self):
        response = self.client.get(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        note = Note.objects.get(pk=self.note.pk)
        serializer = NoteSerializer(note)
        self.assertEqual(response.data, {'note': serializer.data})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_with_invalid_pk(self):
        response = self.client.get(
            reverse('notes_item', kwargs={'pk': 10}),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateNoteTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)

        self.valid_payload = {
            'title': 'test42',
            'content': 'testcontent42'
        }
        self.invalid_payload = {
            'title': '',
            'content': 'testcontent43'
        }

    def test_update_note_with_valid_payload(self):
        response = self.client.put(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note_with_invalid_payload(self):
        response = self.client.put(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleNoteTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        self.note = Note.objects.create(title='test1', content='testcontent1', user=self.user)

    def test_delete_note_with_valid_pk(self):
        response = self.client.delete(
            reverse('notes_item', kwargs={'pk': self.note.pk}),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_note_with_invalid_pk(self):
        response = self.client.delete(
            reverse('notes_item', kwargs={'pk': 10}),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class GetAutoGeneratedNoteTest(APITestCase):
    def setUp(self):
        self.user, self.token_access = set_up_user_with_access_token(self)

        self.note = Note.objects.create(title='Autogenerated Note 1', content='Note content', user=self.user)

    def test_get_autogenerated_note(self):
        response = self.client.post(
            reverse('autogenerated_note'),
            HTTP_AUTHORIZATION=f'JWT {self.token_access}'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
