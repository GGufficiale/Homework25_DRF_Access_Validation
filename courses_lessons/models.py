from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса', help_text='Введите название курса')
    description = models.TextField(max_length=100, verbose_name='Описание курса', help_text='Введите описание курса',
                                   **NULLABLE)
    preview = models.ImageField(upload_to='courses_lessons/course_image', verbose_name='Превью курса',
                                help_text='Загрузите превью курса', **NULLABLE)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название урока', help_text='Введите название урока')
    description = models.TextField(max_length=100, verbose_name='Описание урока', help_text='Введите описание урока',
                                   **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name='Курс', help_text='Выберите курс',
                               **NULLABLE)
    preview = models.ImageField(upload_to='courses_lessons/lesson_image', verbose_name='Превью урока',
                                help_text='Загрузите превью урока', **NULLABLE)
    video = models.TextField(max_length=100, verbose_name='Ссылка на видео', help_text='Вставьте ссылку на видео',
                             **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец урока',
                              help_text="укажите владельца урока")

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
