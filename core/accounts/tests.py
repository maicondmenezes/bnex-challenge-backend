from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

User = get_user_model()


class UserTokenTest(TestCase):
    def test_token_creation_on_user_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertIsInstance(user, User, 'User instance is not created')
        token = Token.objects.filter(user=user).first()
        self.assertIsNotNone(
            token, 'Token was not created for the newly created user'
        )

    def test_no_additional_token_created_on_existing_user_save(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertIsInstance(user, User, 'User instance is not created')

        initial_token_count = Token.objects.filter(user=user).count()
        self.assertEqual(
            initial_token_count,
            1,
            'Initial token was not created for the user',
        )

        user.save()

        updated_token_count = Token.objects.filter(user=user).count()
        self.assertEqual(
            updated_token_count,
            1,
            'An additional token was created on existing user save',
        )


class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345'
        )
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.admin_user = User.objects.create_superuser(
            username='adminuser',
            password='12345',
        )
        self.admin_token, _ = Token.objects.get_or_create(user=self.admin_user)
        self.admin_client = APIClient()
        self.admin_client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.admin_token.key
        )

    def test_api_auth_token_success(self):
        self.user = User.objects.create_user(
            username='testuser2', password='12345'
        )

        response = self.client.post(
            '/api/auth/token/',
            {'username': 'testuser2', 'password': '12345'},
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)

    def test_no_admin_user_try_to_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 403)

    def test_admin_user_try_to_list_users(self):
        response = self.admin_client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_custom_auth_token(self):
        response = self.client.post(
            '/api/auth/token/',
            {
                'username': 'testuser',
                'password': '12345',
                'email': 'test@test.com',
            },
            format='json',
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in response.data)
        self.assertTrue('user_id' in response.data)
        self.assertTrue('email' in response.data)
