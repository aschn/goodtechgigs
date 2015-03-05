from rest_framework import routers
from gigs.views import GigViewSet


router = routers.DefaultRouter()
router.register(r'^', GigViewSet)

urlpatterns = router.urls
