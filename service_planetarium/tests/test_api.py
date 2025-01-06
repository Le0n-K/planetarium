from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from service_planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession, Reservation
from service_planetarium.serializers import ShowThemeSerializer, AstronomyShowListSerializer, PlanetariumDomeSerializer

SHOW_THEME_URL = reverse("service_planetarium:showtheme-list")
ASTRONOMY_SHOW_URL = reverse("service_planetarium:astronomyshow-list")
PLANETARIUM_DOME_URL = reverse("service_planetarium:planetariumdome-list")
SHOW_SESSION_URL = reverse("service_planetarium:showsession-list")
RESERVATION_URL = reverse("service_planetarium:reservation-list")

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(SHOW_THEME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="user@example.com", password="testpass123")
        self.client.force_authenticate(self.user)

    def test_list_show_themes(self):
        ShowTheme.objects.create(name="Space")
        ShowTheme.objects.create(name="Planets")

        res = self.client.get(SHOW_THEME_URL)

        themes = ShowTheme.objects.all().order_by("-name")
        serializer = ShowThemeSerializer(themes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_show_theme_forbidden(self):
        payload = {"name": "Space"}
        res = self.client.post(SHOW_THEME_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_astronomy_shows(self):
        AstronomyShow.objects.create(title="Mars Exploration", description="Journey to Mars")
        AstronomyShow.objects.create(title="Solar System", description="Our cosmic neighborhood")

        res = self.client.get(ASTRONOMY_SHOW_URL)

        shows = AstronomyShow.objects.all().order_by("title")
        serializer = AstronomyShowListSerializer(shows, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_list_planetarium_domes(self):
        PlanetariumDome.objects.create(name="Main Dome", rows=20, seats_in_row=30)
        PlanetariumDome.objects.create(name="Small Dome", rows=10, seats_in_row=20)

        res = self.client.get(PLANETARIUM_DOME_URL)

        domes = PlanetariumDome.objects.all()
        serializer = PlanetariumDomeSerializer(domes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

class AdminApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="admin@example.com", password="testpass123", is_staff=True)
        self.client.force_authenticate(self.user)

    def test_create_show_theme(self):
        payload = {"name": "Space"}
        res = self.client.post(SHOW_THEME_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = ShowTheme.objects.filter(name=payload["name"]).exists()
        self.assertTrue(exists)

    def test_create_astronomy_show(self):
        payload = {
            "title": "Mars Exploration",
            "description": "Journey to Mars",
            "show_theme": []
        }
        res = self.client.post(ASTRONOMY_SHOW_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = AstronomyShow.objects.filter(title=payload["title"]).exists()
        self.assertTrue(exists)

    def test_create_planetarium_dome(self):
        payload = {
            "name": "New Dome",
            "rows": 25,
            "seats_in_row": 40
        }
        res = self.client.post(PLANETARIUM_DOME_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        exists = PlanetariumDome.objects.filter(name=payload["name"]).exists()
        self.assertTrue(exists)
