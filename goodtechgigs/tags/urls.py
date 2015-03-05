from rest_framework import routers
from tags.views import SkillViewSet, CauseViewSet


router = routers.DefaultRouter()
router.register('skills', SkillViewSet)
router.register('causes', CauseViewSet)

urlpatterns = router.urls
