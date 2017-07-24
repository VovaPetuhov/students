from datetime import datetime
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from students.models import Student, Group


class TestStudentList(TestCase):
    def setUp(self):
        group1, created = Group.objects.get_or_create(title='MtM-1')
        group2, created = Group.objects.get_or_create(title='MtM-2')
        Student.objects.get_or_create(first_name='Vitaliy',
                                      last_name='Podoba',
                                      birthday=datetime.today(),
                                      ticket='12345',
                                      student_group=group1)
        Student.objects.get_or_create(first_name='John',
                                      last_name='Dobson',
                                      birthday=datetime.today(),
                                      ticket='23456',
                                      student_group=group2)
        Student.objects.get_or_create(first_name='Sam',
                                      last_name='Stefenson',
                                      birthday=datetime.today(),
                                      ticket='34567',
                                      student_group=group2)
        Student.objects.get_or_create(first_name='Arnold',
                                      last_name='Kidney',
                                      birthday=datetime.today(),
                                      ticket='45678',
                                      student_group=group2)
        self.client = Client()
        self.url = reverse('home')

    def test_students_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Vitaliy', str(response.content))
        self.assertIn(reverse('students_edit', kwargs={'pk': Student.objects.all()[0].id}), str(response.content))
        self.assertEqual(len(response.context['students']), 3)

