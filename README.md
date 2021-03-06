# "Улучшитель оценок 1.0" для электронного дневника
Этот скрипт - фича для того, чтобы пофиксить неудачные оценки, делитнуть несправедливые замечания и разместить-таки заслуженную похвалу в электронном дневнике.

## Перед началом работы
Скрипт бесполезен без самого электронного дневника. В первую очередь устанавливаем его.
Полный репозиторий размещен по ссылке:
https://github.com/devmanorg/e-diary/tree/master
Делаем все по инструкции из `README.md`
Не забываем подключить базу данных, тестовый архив с базой данных доступен по ссылке: 
https://dvmn.org/filer/canonical/1562234129/166/
Скрипт умеет: исправлять плохие оценки, удалять замечания и создавать "похвалу" от учителей в электронном дневнике.

После установки электронного дневника из репозитория и подключения базы данных, последовательно выполняем следующие шаги:
1. Размещаем файл `diary_improver.py` из данного репозитория  в корневую папку Django-проекта электронного дневника, т.е. рядом с файлом `manage.py`.
2. Далее нам потребуется работать из оболочки (shell). Запускаем shell командой в терминале:
`python manage.py shell`
3. Импортируем целиком содержимое файла `diary_improver.py` командой в режиме shell:
`from diary_improver import *` Теперь мы получили доступ непосредственно к коду нашего улучшителя.
4. В этом шаге нужно получить доступ к объекту искомого ученика, успеваемость которого мы собираемся "корректировать" и запомнить его в переменной `schoolkid`. Для этого непосредственно в shell мы выполняем следующие команды: 
```schoolkid = Schoolkid.objects.filter(full_name='Фомичев Ким Елисеевич', year_of_study=1, group_letter='А').first()```

В данном коде: `full_name` - это имя ученика в формате 'Фамилия Имя Отчество',
`year_of_study` - это класс ученика (год обучения от 1 до 10),
`group_letter` - это "буква" класса (кириллицей!), в котором учиться наш искомый ученик.
Не забываем ставить кавычки ' '.


## Функционал скрипта

### Исправляем плохие оценки
Работаем в shell, предварительно выполнив шаги, указанные в разделе "Перед началом работы".
Чтобы исправить плохие отметки,используем следующую функцию: `fix_marks(schoolkid)` В качестве аргумента функции `fix_marks` мы передаем объект нашего ученика, полученный в шаге 4.
Все оценки нашего ученика, переданного в переменную `schoolkid` (кроме "4" и "5") по всем предметам  будут заменены на "5". 

### Удаляем замечания
Работаем в shell, предварительно выполнив шаги, указанные в разделе "Перед началом работы".
Для удаления замечаний используйте функцию `remove_chastisements(schoolkid)` Все замечания нашего ученика, переданного в переменную `schoolkid` по всем предметам будут автоматически удалены. 

### Создаем заслуженную похвалу
Работаем в shell, предварительно выполнив шаги, указанные в разделе "Перед началом работы". 
За создание похвалы отвечает функция `create_commendation(schoolkid_name, subject_title)`
Применяя эту функцию, в отличие от предыдущих, достаточно указать имя ученика `schoolkid_name` (а не передавать функции объект ученика `schoolkid`) и указать в аргумент
`subject_title` наименование предмета, по которому будет создана похвала.
Функция `create_commendation` осуществляет автоматическую проверку: если программа не найдет ни одного ученика по заданному Вами имени она выведет следующее сообщение:
 "Ученик с таким именем не найден. Проверьте орфографию.".
В случае, если Вы укажете имя ученика, которое носят 2 и более учащихся, программа сообщит об ошибке:: "Найдено несколько учеников по критерию поиска. Уточните имя/фамилию ученика."
Аналогичным образом программа сообщит об ошибке, если Вы некорректно укажете название предмета, по которому необходимо создать похвалу: "Не найдено ни одного занятия по заданному предмету. Проверьте орфографию написания предмета."

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
