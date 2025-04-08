from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "age": 25,
            "gender": "Male",
        }

    def test_create_user(self):
        response = self.client.post("/users/", self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team_data = {
            "team_name": "Team A",
            "members": [],
        }

    def test_create_team(self):
        response = self.client.post("/teams/", self.team_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# Similar test cases can be added for Activity, Leaderboard, and Workout APIs.
