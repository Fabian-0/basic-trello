from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class UserTestCase(APITestCase):

    BASE_URL = 'http://127.0.0.1:8000'

    USER_DATA_TEST = {
        'username': 'testUser',
        'password': 'password',
        'first_name' : 'User',
        'email' : 'user@gmail.com',
        'last_name' : 'Lastname',
    }

    def setUp(self) -> None:

        user = User.objects.create_user( username='userTest', password='password')
        #user_two = User.objects.create_user( username='userTestTwo', password='password')

        auth_response = self.client.post(f'{self.BASE_URL}/api/token/', data={'username': 'userTest', 'password': 'password'})
        token = auth_response.data.get('access')

        self.assertEqual(auth_response.status_code, 200)
        self.assertIsNotNone(token)

        self.user = user
        self.token = f'Bearer {token}'

        patch_response = self.client.patch(
            f'{self.BASE_URL}/users/{self.user_id}/',
            data={
                'password': 'password',
            },
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

        self.assertEqual(patch_response.status_code, 200)

        self.user_id = patch_response.data.get('id')
    
    # Post tests

    def test_get_user(self):
        response = self.client.get(f'{self.BASE_URL}/users/')
        print(response.data)
        
        self.assertEqual(response.status_code, 401)

    def test_create_correctly(self):
        create_response = self.client.post(
            f'{self.BASE_URL}/users/',
            data=self.USER_DATA_TEST,
        )
        print(create_response.data)

        self.assertEqual(create_response.status_code, 201)

    def test_update_permission(self):
        update_response = self.client.patch(
            f'{self.BASE_URL}/users/{self.user_id}/',
            data={
                'password': 'password',
            },
            HTTP_AUTHORIZATION=self.token
    )
        self.assertEqual(update_response.status_code, 201)

