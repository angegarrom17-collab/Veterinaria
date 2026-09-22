Pasos para instalar dependencias, migrar y ejecutar:

1.	Crear y activar el entorno virtual: python -m venv .venv
2.	Instalar dependencias: pip install django djangorestframework django-filter
3.	Aplicar las migraciones de la base de datos:
python manage.py makemigrations
python manage.py migrate
4.	Crear un superusuario: 
python manage.py createsuperuser
5.	Ejecutar el servidor de desarrollo: python manage.py runserver

REFLEXION:

El flujo comienza cuando Postman manda una petición POST a la URL del sistema de veterinaria. Esa petición llega a la View, la cual se apoya en el Serializer para revisar que los datos estén bien mediante la validación. Luego, el Serializer le pasa la información al Model, y gracias al ORM se arman y ejecutan las consultas necesarias en la base de datos. Por último, la View devuelve una Response en formato JSON confirmando que todo salió bien.
