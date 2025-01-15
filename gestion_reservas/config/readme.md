# Proyecto de Gestión de Reservas

## Descripción General

Este proyecto permite la gestión de reservas de salas en un entorno educativo o de oficina. Los usuarios pueden hacer reservas de salas, ver la disponibilidad de las mismas, y evitar conflictos de horarios mediante la validación de los tiempos de reserva. El sistema está implementado con Django y utiliza una base de datos PostgreSQL.

## Pasos para la Instalación y Configuración del Entorno

1. **Clonar el Repositorio**

   Clona el repositorio de GitHub:

   ```bash
   git clone https://github.com/lmendozam1983/gestion_reservas.git
   cd gestion_reservas

2. **Crear y Activar el Entorno Virtual**

    En el directorio del proyecto, crea un entorno virtual para evitar conflictos con las dependencias del sistema:

    ```bash
    mkvirtualenv gestion_reservas
    workon gestion_reservas

3.  **Instalar las Dependencias**

    Instala las dependencias del proyecto desde el archivo requirements.txt:

    ```bash
    pip install -r requirements.txt

## Instalar PostgreSQL

Si aún no tienes PostgreSQL instalado, sigue los pasos en la documentación oficial de PostgreSQL para instalarlo en tu sistema operativo.

## Configurar la Base de Datos

1.  Crea una base de datos para el proyecto. Abre la terminal de PostgreSQL:

     ```bash
    sudo -u postgres psql

2.  Luego, ejecuta los siguientes comandos para crear una base de datos y un usuario:

     ```bash    
    CREATE DATABASE gestion_reservas;
    CREATE USER gestor WITH PASSWORD 'tu_contraseña';
    ALTER ROLE gestor SET client_encoding TO 'utf8';
    ALTER ROLE gestor SET default_transaction_isolation TO 'read committed';
    ALTER ROLE gestor SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE gestion_reservas TO gestor;
    \q

3.  Configurar el archivo **settings.py** en Django

En el archivo settings.py de tu proyecto Django, configura la base de datos PostgreSQL con los datos creados anteriormente:

    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'gestion_reservas',
            'USER': 'gestor',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

## Instrucciones para Ejecutar el Proyecto y Cargar Datos Iniciales

1.  Migrar la Base de Datos

Ejecuta las migraciones para configurar las tablas de la base de datos:

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate

2.  Ejecutar el Servidor de Desarrollo

Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:

    
    python manage.py runserver

## Dependencias del Proyecto

Este proyecto utiliza las siguientes dependencias. Puedes verlas en el archivo requirements.txt y instalarlas con pip:

    ```bash
    asgiref==3.8.1
    beautifulsoup4==4.12.3
    crispy-bootstrap5==2024.10
    Django==4.2.18
    django-bootstrap-v5==1.0.11
    django-crispy-forms==2.3
    psycopg==3.2.3
    soupsieve==2.6
    sqlparse==0.5.3
    typing_extensions==4.12.2

Se pueden instalar todas las dependencias usando el archivo requirements.txt, usando el siguinete comando:

    ```bash
    pip install -r requirements.txt


## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Creado por LMM.



