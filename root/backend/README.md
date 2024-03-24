# setting up backend

~\root\backend

```
python -m venv venv
venv\Scripts\activate
pip install django
django-admin startproject myproject .
pip install django djangorestframework
python manage.py migrate
python manage.py createsuperuser
python runserver
```