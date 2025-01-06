from rest_framework import routers

from service_planetarium.views import (
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    AstronomyShowViewSet,
    ShowSessionViewSet,
    ReservationViewSet,

)

router = routers.DefaultRouter()
router.register("showthemes", ShowThemeViewSet, basename="showtheme")
router.register("planetariumdomes", PlanetariumDomeViewSet, basename="planetariumdome")
router.register("astronomyshows", AstronomyShowViewSet, basename="astronomyshow")
router.register("showsessions", ShowSessionViewSet, basename="showsession")
router.register("reservations", ReservationViewSet, basename="reservation")

urlpatterns = router.urls

app_name = "service_planetarium"
