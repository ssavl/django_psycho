# django_psycho
test project - Vue.js | PosgreSQL | Django


## Установка виртуального окружения 

> virtualenv venv

> pip install -r requirements.txt

> cd vue

> npm install

## Запуск проекта

/django_psycho

> python manage.py runserver

/vue

> npm run serve

## Кастомная команда для синхронизации данных с сервисом AirTable

> python manage.py upload_airtable

#### Благодаря костомной команде "джобе" программа запускает скрипт который:

1. Создает дамп "сырых" данных в базу.
2. Изменяет текущие данные так, чтобы в базе в отдельной таблице 
   хранились данные только в таком виде, в котором они находятся в AirTable.
   
3. Скрипт Добавляет или изменяет методы Психологов, их фото и имена.


![alt tag](https://doc-0o-88-docs.googleusercontent.com/docs/securesc/fjl2rrbj4uhcro3e20kn7bto1987o696/eqq7nsjgjc833jo4uli0v9s1cke4hdr3/1612789200000/04770584948946926459/04770584948946926459/1A7UdZXoASZHpGb5R3P9O0nTHFB8d6cMr?e=view&authuser=0&nonce=30emm4pnrl91i&user=04770584948946926459&hash=qbg2frctm7k6vs727q3o21in98ucn067 "Верстка по мокапу")​



PS В качестве дополнительного фреймворка для фронта был использован Bootstrap 
