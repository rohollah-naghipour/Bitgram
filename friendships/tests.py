from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import Friendship

User = get_user_model()


class SendFriendRequestViewTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', 
            email='user1@test.com', 
            password='testpass123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='testpass123'
        )
        self.user3 = User.objects.create_user(
            username='user3',
            email='user3@test.com',
            password='testpass123'
        )
        
        self.client.force_authenticate(user=self.user1)

    def test_send_friend_request_success(self):
        url = reverse('send-friend-request')
        data = {'user': self.user2.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['detail'], "Request sent")
        self.assertTrue(Friendship.objects.filter(
            request_from=self.user1,
            request_to=self.user2
        ).exists())

    def test_send_friend_request_to_self(self):
        url = reverse('send-friend-request')
        data = {'user': self.user1.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['message'],
            'You cannot send yourself a friend request'
        )

    def test_send_duplicate_friend_request(self):
        Friendship.objects.create(
            request_from=self.user1,
            request_to=self.user2
        )
        
        url = reverse('send-friend-request')
        data = {'user': self.user2.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(
            response.data['message'],
            'Friend request has already been sent'
        )

    def test_send_request_when_reverse_exists(self):
        Friendship.objects.create(
            request_from=self.user2,
            request_to=self.user1
        )
        
        url = reverse('send-friend-request')
        data = {'user': self.user2.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(
            response.data['message'],
            'You have already received a friend request from this user'
        )

    def test_send_request_unauthenticated(self):
        self.client.logout()  
        
        url = reverse('send-friend-request')
        data = {'user': self.user2.id}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_send_request_to_nonexistent_user(self):
        url = reverse('send-friend-request')
        data = {'user': 9999}  
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)