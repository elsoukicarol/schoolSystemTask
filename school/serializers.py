# Import the serializers from the rest_framework library
from rest_framework import serializers

# Import the models of which we are going to create the serializers
from .models import Address, Student, Subject, Enrollment


class AddressSerializer(serializers.ModelSerializer):
    # The class Meta tells the model what to use and what fields to serialize
    class Meta:
        model = Address
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # We can specify the fields we want, or we can print them all like in the above serializer
        fields = ['name', 'age', 'address']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
