from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, StudentViewSet, SubjectViewSet, EnrollmentViewSet
from django.urls import path, include

# We use default router because it automatically creates URL routes for viewsets.
router = DefaultRouter()
router.register('address', AddressViewSet)
router.register('students', StudentViewSet)
router.register('subjects', SubjectViewSet)
router.register('enrollment', EnrollmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]