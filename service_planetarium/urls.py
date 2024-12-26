from django.urls import path, include
from rest_framework import routers

from service_planetarium.views import (
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    AstronomyShowViewSet,
    ShowSessionViewSet,
    ReservationViewSet,

)

router = routers.DefaultRouter()
router.register("show-themes", ShowThemeViewSet)
router.register("planetarium-domes", PlanetariumDomeViewSet)
router.register("astronomy-shows", AstronomyShowViewSet)
router.register("show-sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "service_planetarium"
