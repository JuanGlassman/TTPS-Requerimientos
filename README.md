# TTPS-Requerimientos

### Help
- Para preparar las migraciones
```~$ python manage.py makemigrations```


- Para hacer las migraciones
```~$ python manage.py migrate```

- Para hacer seed de la base de datos
```~$ python manage.py shell```
```
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from TTPS.seeds import run_seeds
>>> run_seeds()
```

- Para correr la apliacion
```~$ python manage.py runserver```