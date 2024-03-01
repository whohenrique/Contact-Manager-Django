from rest_framework.routers import DefaultRouter
from .viewsSet import ContactsViewSet

router = DefaultRouter()
router.register(r'contact', ContactsViewSet, basename='contacts')
urlpatterns = router.urls