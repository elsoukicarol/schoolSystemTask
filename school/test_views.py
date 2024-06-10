import pytest
from rest_framework.test import APIClient
from .models import Address, Student, Subject, Enrollment


@pytest.fixture
def api_client():
    return APIClient()


# Address tests
@pytest.mark.django_db
def test_create_address(api_client):
    response = api_client.post('/schoolSystem/address/',
                               {'address': '123 Main St', 'city': 'Springfield', 'zip_code': '12345'}, format='json')
    assert response.status_code == 201
    assert Address.objects.count() == 1
    assert Address.objects.get().city == 'Springfield'


@pytest.mark.django_db
def test_get_address(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    response = api_client.get(f'/schoolSystem/address/{address.id}/')
    assert response.status_code == 200
    assert response.data['city'] == 'Springfield'


@pytest.mark.django_db
def test_update_address(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    response = api_client.put(f'/schoolSystem/address/{address.id}/',
                              {'address': '456 Elm St', 'city': 'Metropolis', 'zip_code': '54321'}, format='json')
    assert response.status_code == 200
    address.refresh_from_db()
    assert address.city == 'Metropolis'


@pytest.mark.django_db
def test_delete_address(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    response = api_client.delete(f'/schoolSystem/address/{address.id}/')
    assert response.status_code == 204
    assert Address.objects.count() == 0


# Student tests
@pytest.mark.django_db
def test_create_student(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    response = api_client.post('/schoolSystem/students/',
                               {'name': 'John Doe', 'age': '20', 'address': address.id}, format='json')
    assert response.status_code == 201
    assert Student.objects.count() == 1
    assert Student.objects.get().name == 'John Doe'


@pytest.mark.django_db
def test_get_student(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    response = api_client.get(f'/schoolSystem/students/{student.id}/')
    assert response.status_code == 200
    assert response.data['name'] == 'John Doe'


@pytest.mark.django_db
def test_update_student(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    response = api_client.put(f'/schoolSystem/students/{student.id}/',
                              {'name': 'Jane Doe', 'age': '21', 'address': address.id}, format='json')
    assert response.status_code == 200
    student.refresh_from_db()
    assert student.name == 'Jane Doe'
    assert student.age == '21'


@pytest.mark.django_db
def test_delete_student(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    response = api_client.delete(f'/schoolSystem/students/{student.id}/')
    assert response.status_code == 204
    assert Student.objects.count() == 0


# Subject tests
@pytest.mark.django_db
def test_create_subject(api_client):
    response = api_client.post('/schoolSystem/subjects/',
                               {'name': 'Math', 'credits': '3'}, format='json')
    assert response.status_code == 201
    assert Subject.objects.count() == 1
    assert Subject.objects.get().name == 'Math'


@pytest.mark.django_db
def test_get_subject(api_client):
    subject = Subject.objects.create(name='Math', credits='3')
    response = api_client.get(f'/schoolSystem/subjects/{subject.id}/')
    assert response.status_code == 200
    assert response.data['name'] == 'Math'


@pytest.mark.django_db
def test_update_subject(api_client):
    subject = Subject.objects.create(name='Math', credits='3')
    response = api_client.put(f'/schoolSystem/subjects/{subject.id}/',
                              {'name': 'Science', 'credits': '4'}, format='json')
    assert response.status_code == 200
    subject.refresh_from_db()
    assert subject.name == 'Science'
    assert subject.credits == '4'


@pytest.mark.django_db
def test_delete_subject(api_client):
    subject = Subject.objects.create(name='Math', credits='3')
    response = api_client.delete(f'/schoolSystem/subjects/{subject.id}/')
    assert response.status_code == 204
    assert Subject.objects.count() == 0


# Enrollment tests
@pytest.mark.django_db
def test_create_enrollment(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    subject = Subject.objects.create(name='Math', credits='3')
    response = api_client.post('/schoolSystem/enrollment/',
                               {'student': student.id, 'subject': subject.id, 'enrollmentDate': '2024-01-01T00:00:00Z',
                                'grade': 95.0}, format='json')
    assert response.status_code == 201
    assert Enrollment.objects.count() == 1
    assert Enrollment.objects.get().grade == 95.0


@pytest.mark.django_db
def test_get_enrollment(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    subject = Subject.objects.create(name='Math', credits='3')
    enrollment = Enrollment.objects.create(student=student, subject=subject, enrollmentDate='2024-01-01T00:00:00Z',
                                           grade=95.0)
    response = api_client.get(f'/schoolSystem/enrollment/{enrollment.id}/')
    assert response.status_code == 200
    assert response.data['grade'] == 95.0


@pytest.mark.django_db
def test_update_enrollment(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    subject = Subject.objects.create(name='Math', credits='3')
    enrollment = Enrollment.objects.create(student=student, subject=subject, enrollmentDate='2024-01-01T00:00:00Z',
                                           grade=95.0)
    response = api_client.put(f'/schoolSystem/enrollment/{enrollment.id}/',
                              {'student': student.id, 'subject': subject.id, 'enrollmentDate': '2024-01-01T00:00:00Z',
                               'grade': 90.0}, format='json')
    assert response.status_code == 200
    enrollment.refresh_from_db()
    assert enrollment.grade == 90.0


@pytest.mark.django_db
def test_delete_enrollment(api_client):
    address = Address.objects.create(address='123 Main St', city='Springfield', zip_code='12345')
    student = Student.objects.create(name='John Doe', age='20', address=address)
    subject = Subject.objects.create(name='Math', credits='3')
    enrollment = Enrollment.objects.create(student=student, subject=subject, enrollmentDate='2024-01-01T00:00:00Z',
                                           grade=95.0)
    response = api_client.delete(f'/schoolSystem/enrollment/{enrollment.id}/')
    assert response.status_code == 204
    assert Enrollment.objects.count() == 0
