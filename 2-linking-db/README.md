### Connect to data base
in `atato_django_demo` change
``` py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
to
``` py
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

### Start Django Project
Outside SSH

```sh
$ docker-compose up
```

You should be able yo visit website on `localhost:8000`

Note in `settings.py` you can add `ALLOWED_HOSTS` = ['0.0.0.0']

SSH
in another tab while docker-compose is running
```sh
docker exec -it django_demo_web bash
```
