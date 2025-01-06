from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime, timedelta

from service_planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession, Reservation

User = get_user_model()

class ViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(email="testuser@example.com", password="testpass")
        self.admin_user = User.objects.create_superuser(email="admin@example.com", password="adminpass")
        self.show_theme = ShowTheme.objects.create(name="Theme 1")
        self.astronomy_show1 = AstronomyShow.objects.create(title="Solar System", description="Our cosmic neighborhood")
        self.astronomy_show2 = AstronomyShow.objects.create(title="Galaxies", description="Island universes")
        self.planetarium_dome = PlanetariumDome.objects.create(name="Main Dome", rows=20, seats_in_row=30)

    def test_create_show_theme_unauthorized(self):
        url = reverse("service_planetarium:showtheme-list")
        data = {"name": "Educational"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_show_theme_authorized(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse("service_planetarium:showtheme-list")
        data = {"name": "Educational"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_astronomy_shows(self):
        self.astronomy_show1.show_theme.add(self.show_theme)
        self.astronomy_show2.show_theme.add(self.show_theme)

        url = reverse("service_planetarium:astronomyshow-list")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_reservation(self):
        self.client.force_authenticate(user=self.user)
        show_session = ShowSession.objects.create(
            show_time=datetime.now() + timedelta(days=3),
            astronomy_show=self.astronomy_show1,
            planetarium_dome=self.planetarium_dome
        )

        url = reverse("service_planetarium:reservation-list")
        data = {
            "tickets": [
                {"row": 5, "seat": 10, "show_session": show_session.id}
            ]
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_reservations(self):
        self.client.force_authenticate(user=self.user)
        Reservation.objects.create(user=self.user)

        url = reverse("service_planetarium:reservation-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
