from rest_framework import routers
from .views import WalletsViewSet

router = routers.DefaultRouter()
router.register(r'wallets', WalletsViewSet, basename='wallets')
urlpatterns = router.urls
