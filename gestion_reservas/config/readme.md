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
python3 -m venv venv
source venv/bin/activate  # En Windows usa: venv\Scripts\activate

Instalar las Dependencias

Instala las dependencias del proyecto desde el archivo requirements.txt:
pip install -r requirements.txt

Instalar PostgreSQL

Si aún no tienes PostgreSQL instalado, sigue los pasos en la documentación oficial de PostgreSQL para instalarlo en tu sistema operativo.

Configurar la Base de Datos

Crea una base de datos para el proyecto. Abre la terminal de PostgreSQL:
sudo -u postgres psql

Luego, ejecuta los siguientes comandos para crear una base de datos y un usuario:

CREATE DATABASE gestion_reservas;
CREATE USER gestor WITH PASSWORD 'tu_contraseña';
ALTER ROLE gestor SET client_encoding TO 'utf8';
ALTER ROLE gestor SET default_transaction_isolation TO 'read committed';
ALTER ROLE gestor SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gestion_reservas TO gestor;
\q

Configurar el archivo settings.py en Django

En el archivo settings.py de tu proyecto Django, configura la base de datos PostgreSQL con los datos creados anteriormente:
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

Instrucciones para Ejecutar el Proyecto y Cargar Datos Iniciales
Migrar la Base de Datos

Ejecuta las migraciones para configurar las tablas de la base de datos:
python manage.py migrate

Cargar Datos Iniciales (Opcional)

Si deseas cargar datos iniciales, por ejemplo, para crear algunas salas de ejemplo, puedes utilizar un archivo de fixtures o crear las entradas desde el panel de administración de Django. Para cargar un archivo de fixtures:
python manage.py loaddata fixtures/archivo_de_datos_iniciales.json

Ejecutar el Servidor de Desarrollo

Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:
python manage.py runserver

Dependencias del Proyecto
Este proyecto utiliza las siguientes dependencias. Puedes verlas en el archivo requirements.txt y instalarlas con pip:

Django==3.2
psycopg2==2.9.3
djangorestframework==3.12.4
otras dependencias que puedas estar utilizando
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


### 2. Archivo `requirements.txt`

Este archivo debe incluir todas las dependencias necesarias para que tu proyecto funcione correctamente. Aquí tienes un ejemplo básico:

```txt
Django==3.2
psycopg2==2.9.3
djangorestframework==3.12.4

