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


PS В качестве дополнительного фреймворка для фронта был использован Bootstrap 