from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Chastisement, Commendation, Lesson, Mark,\
    Schoolkid


encouragements = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь! что нужно',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def fix_marks(schoolkid):
    schoolkid_marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for schoolkid_mark in schoolkid_marks:
        schoolkid_mark.points = 5
        schoolkid_mark.save()


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid_name, subject_title):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except ObjectDoesNotExist:
        exit('Ученик с таким именем не найден. Проверьте орфографию.')
    except MultipleObjectsReturned:
        exit("""Найдено несколько учеников по критерию поиска.
        Уточните имя/фамилию ученика.""")
    schoolkid_subject_lessons = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject_title
    )
    lesson = schoolkid_subject_lessons.order_by('?').first()

    if not lesson:
        exit("""Не найдено ни одного занятия по заданному предмету.
        Проверьте орфографию написания предмета.""")

    Commendation.objects.create(
        text=choice(encouragements),
        schoolkid=schoolkid,
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date
    )
