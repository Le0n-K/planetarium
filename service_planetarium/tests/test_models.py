from django.test import TestCase
from django.contrib.auth import get_user_model
from service_planetarium.models import ShowTheme, AstronomyShow, PlanetariumDome, ShowSession, Reservation, Ticket

class ModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="testpass123"
        )

    def test_show_theme_str(self):
        theme = ShowTheme.objects.create(name="Space Exploration")
        self.assertEqual(str(theme), "Space Exploration")

    def test_astronomy_show_str(self):
        show = AstronomyShow.objects.create(
            title="Journey to Mars",
            description="Explore the Red Planet"
        )
        self.assertEqual(str(show), "Journey to Mars")

    def test_planetarium_dome_str(self):
        dome = PlanetariumDome.objects.create(
            name="Main Dome",
            rows=20,
            seats_in_row=30
        )
        self.assertEqual(str(dome), "Main Dome")
        self.assertEqual(dome.capacity, 600)

    def test_show_session_str(self):
        show = AstronomyShow.objects.create(
            title="Journey to Mars",
            description="Explore the Red Planet"
        )
        dome = PlanetariumDome.objects.create(
            name="Main Dome",
            rows=20,
            seats_in_row=30
        )
        session = ShowSession.objects.create(
            show_time="2023-05-01 14:00:00",
            astronomy_show=show,
            planetarium_dome=dome
        )
        self.assertEqual(str(session), "Journey to Mars 2023-05-01 14:00:00")

    def test_reservation_str(self):
        reservation = Reservation.objects.create(user=self.user)
        self.assertTrue(str(reservation).startswith(str(reservation.created_at)))

    def test_ticket_str(self):
        show = AstronomyShow.objects.create(
            title="Journey to Mars",
            description="Explore the Red Planet"
        )
        dome = PlanetariumDome.objects.create(
            name="Main Dome",
            rows=20,
            seats_in_row=30
        )
        session = ShowSession.objects.create(
            show_time="2023-05-01 14:00:00",
            astronomy_show=show,
            planetarium_dome=dome
        )
        reservation = Reservation.objects.create(user=self.user)
        ticket = Ticket.objects.create(
            row=5,
            seat=10,
            show_session=session,
            reservation=reservation
        )
        self.assertEqual(str(ticket), "Journey to Mars 2023-05-01 14:00:00 (row: 5, seat: 10)")
