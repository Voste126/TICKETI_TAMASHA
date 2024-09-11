from rest_framework import status
from rest_framework.test import APITestCase

class HomeViewTestCase(APITestCase):
    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Welcome to Django Daraja API'})

class STKPushViewTestCase(APITestCase):
    def test_stk_push_view(self):
        response = self.client.post('/stk-push/', {'amount': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on the expected response

class OAuthSuccessViewTestCase(APITestCase):
    def test_oauth_success_view(self):
        response = self.client.get('/oauth-success/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on the expected response