from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from courses_lessons.models import Course, Lesson, Subscription
from courses_lessons.validators import YoutubeValidators


class LessonSerializer(ModelSerializer):
    validators = [YoutubeValidators(field='video_url')]

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    validators = [YoutubeValidators(field='video_url')]

    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(ModelSerializer):
    # кастомный атрибут для вывода инфо по к-ву уроков в курсе
    amount_of_lessons_in_course = SerializerMethodField()
    lesson_info = SerializerMethodField(read_only=True)

    def get_amount_of_lessons_in_course(self, course):
        """Метод подсчета к-ва уроков в курсе"""
        return Lesson.objects.filter(course=course).count()

    def get_lesson_info(self, course):
        """Метод вывода инфы об уроках в курсе"""
        lessons_set = Lesson.objects.filter(course=course)
        return [(lesson.name, lesson.description) for lesson in lessons_set]

    class Meta:
        model = Course
        fields = ('name', 'description', 'lesson_info', 'amount_of_lessons_in_course')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
