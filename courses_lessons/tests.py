from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from courses_lessons.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='django@mail.ru')
        self.course = Course.objects.create(name='course_test')
        self.lesson = Lesson.objects.create(name='lesson_test', description='test description')
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("courses_lessons:lesson_get", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.title)
