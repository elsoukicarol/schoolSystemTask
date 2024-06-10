from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import AddressFilter, StudentFilter, SubjectFilter, EnrollmentFilter
from .models import Address, Student, Subject, Enrollment
from .serializers import AddressSerializer, StudentSerializer, SubjectSerializer, EnrollmentSerializer


# This query set provides all CRUD operations
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AddressFilter

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubjectFilter


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EnrollmentFilter
