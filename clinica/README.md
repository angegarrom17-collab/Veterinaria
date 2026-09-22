Pasos para instalar dependencias, migrar y ejecutar:

1.	Crear y activar el entorno virtual: python -m venv .venv
2.	Instalar dependencias: pip install django djangorestframework django-filter
3.	Aplicar las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate
4.	Crear un superusuario: 
python manage.py createsuperuser
5.	Ejecutar el servidor de desarrollo: python manage.py runserver
