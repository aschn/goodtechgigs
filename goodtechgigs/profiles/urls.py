from rest_framework import routers
from profiles.views import GigSeekerViewSet, GigPosterViewSet


router = routers.DefaultRouter()
router.register('orgs', GigPosterViewSet)
router.register('helpers', GigSeekerViewSet)

urlpatterns = router.urls
