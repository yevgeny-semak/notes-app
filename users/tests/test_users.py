from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagerTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='test', email='test@localhost', password='1234')

        self.assertEqual(user.email, 'test@localhost')
        self.assertEqual(user.username, 'test')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='test@localhost', username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='test@localhost', username='', password='1234')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', username='test', password='1234')

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(username='supertest', email='supertest@localhost', password='1234')

        self.assertEqual(superuser.email, 'supertest@localhost')
        self.assertEqual(superuser.username, 'supertest')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='supertest@localhost', username='supertest', password='1234',
                                          is_superuser=False)
