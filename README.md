## Задание:

Сделать бота с телефонным справочником

Название чата бота: *HomeWork_NGor_bot*

user_name: *@pot_example_sem_9_bot*

Бот выполняет следующие команды:

1. **/start** - начало работы.

2. **/help** - показывает команнды для работы со справочником.

3. **/all** - показывает весь список контактов.

4. **/find_nam "Имя контакта"** - найти контакт по имени.

5. **/find_comment "Название группы (семья, друзья, работа)"** - все контакты выбранной группы 

6. **/find_phone "Номер телефона"** - найти контакт по номеру телефона 

7. **/delete "Имя контакта"** - удаляет контакт с данным имененм 

8. **/add name; phone; birthday; group** - добавляет контакт с введенными данными именно в этом порядке и через ";"

Телефонный справочник представляет собой базу данных *phone_book.db*, в которую входят две таблицы: *people* и *phones*.

Таблица *people* содержит следующие столбцы:

1. id_people
2. name
3. birthday
4. comment

Таблица *phones* содержит следующие столбцы:

1. id_phone
2. id_people
3. number_phone

Таблицы связаны по столбцу *id_people*.

Каждая функция обращается к модулю logger, который записывает время, имя пользователя, его id и текст сообщения в файл 'db.csv'.