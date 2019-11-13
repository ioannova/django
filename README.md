## 1. Dockerfile

```
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

## 2. requirements.txt

```
Django>=2.0,<3.0
psycopg2>=2.7,<3.0

```

## 3. docker-compose

```
version: '3'

services:
  db:
    image: postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```


## 4. Create project

`docker-compose run web django-admin startproject myproject .`

## 5. Connect project on database postgres

`$vim composeexample/settings.py`

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

## 6. Running project

`docker-compose up`


## 7. Add user permission for projet

`sudo chown -R $USER:USER .`
