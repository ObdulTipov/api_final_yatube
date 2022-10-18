### Проект «API для Yatube»

```
Позволяет клиенту обращаться к приложению, использую протокол HTTP, передавая данные в JSON формате.
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ObdulTipov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Протестируйте API через Postman или отправьте запросы через другие программы:
(Данный запрос должен вернуть список постов из базы данных)

```
GET http://127.0.0.1:8000/api/v1/posts/
```

Можете посмотреть комментарии к посту 1:

```
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

При создании данного проекта использовались библиотеки:

```
Django REST Framework
Djoser
Simple JWT
```

Автор:

```
Ivan M.
```