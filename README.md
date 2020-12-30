# SIMPLE PASSWORD GENERATOR

Generador de contraseñas usando [Django](https://www.djangoproject.com/) y guiandome del curso [Django 3 - Full Stack Websites with Python Web Development](https://zappycode.com/courses/django-3-make-websites-with-python-tutorial-beginner-learn-bootstrap).

## REQUISITOS

Usar pip para instalar las librerias con las que se realizo este pequeño proyecto.

1. activa tu ambiente virtual.
2. cd hasta ubicarte en el directorio en donde requirements.txt se ubica.
3. ejecuta en la consola la siguiete sentencia:

```
pip install -r requirements.txt
```

## PARTICULARIDADES

Se usa un formulario con el metodo GET para generar la contraseña. Para transportar la contraseña desde su generación en el backend hasta mostrarla en el frontend se hace uso de un view en el action del formulario.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)