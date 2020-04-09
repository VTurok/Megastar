from rest_framework.routers import DefaultRouter

from library.views import WritersBooksViewSet

router = DefaultRouter()
router.register("writer", WritersBooksViewSet, basename='Библиотека')
urlpatterns = router.urls
