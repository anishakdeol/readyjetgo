from rest_framework import routers
from .api import TravelViewSet

router = routers.DefaultRouter()
router.register('api/travel', TravelViewSet, 'travel')

urlpatterns = router.urls
