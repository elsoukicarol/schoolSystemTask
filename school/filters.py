import django_filters
from .models import Address, Student, Subject, Enrollment


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        # Defines the fields that can be used for filtering
        fields = {
            'city': ['exact', 'icontains'],
            'zip_code': ['exact', 'icontains'],
        }


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['exact', 'icontains'],
            # gle = greater than or equal
            # lte = lestt than or equal
            'age': ['exact', 'gte', 'lte'],
            # Taking the city attribute from address and filtering according to it
            'address__city': ['exact', 'icontains'],  # Filtering by related model fields
        }


class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = {
            'name': ['exact', 'icontains'],
            'credits': ['exact', 'gte', 'lte'],
        }


class EnrollmentFilter(django_filters.FilterSet):
    class Meta:
        model = Enrollment
        fields = {
            'student__name': ['exact', 'icontains'],
            'subject__name': ['exact', 'icontains'],
            'enrollmentDate': ['exact', 'gte', 'lte'],
            'grade': ['exact', 'gte', 'lte'],
        }
