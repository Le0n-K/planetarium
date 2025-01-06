from django.test import TestCase
from django.contrib.auth import get_user_model

from service_planetarium.serializers import (
    ShowThemeSerializer,
    PlanetariumDomeSerializer,
    AstronomyShowSerializer
)

User = get_user_model()

class SerializerTests(TestCase):
    def test_show_theme_serializer(self):
        theme_data = {"name": "Adventure"}
        serializer = ShowThemeSerializer(data=theme_data)
        self.assertTrue(serializer.is_valid())

    def test_planetarium_dome_serializer(self):
        dome_data = {"name": "Small Dome", "rows": 5, "seats_in_row": 10}
        serializer = PlanetariumDomeSerializer(data=dome_data)
        self.assertTrue(serializer.is_valid())

    def test_astronomy_show_serializer(self):
        show_data = {"title": "Black Holes", "description": "Mysteries of the universe"}
        serializer = AstronomyShowSerializer(data=show_data)
        self.assertTrue(serializer.is_valid())
