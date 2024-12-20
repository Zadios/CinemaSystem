# CinemaRoyale

CinemaRoyale es un sistema desarrollado como parte de una tesis para la carrera "Analista de Sistemas". Este sistema permite gestionar un cine, incluyendo la administración de películas, salas, funciones, promociones, tickets y un sistema básico de usuarios.

## Requisitos Previos

- **Python 3.x** (se recomienda la última versión estable).
- **Django**: Framework web utilizado para desarrollar el sistema.
- **PostgreSQL**: Base de datos relacional que se usa para almacenar la información.

## Instrucciones de Instalación

### 1. Clonar el Repositorio

Descargar el proyecto desde su repositorio correspondiente y guardar los archivos en su máquina local.

### 2. Crear un Entorno Virtual

Para gestionar las dependencias del proyecto, es necesario crear un entorno virtual utilizando `venv`. Esto puede hacerse con el comando adecuado para el sistema operativo en uso. Una vez creado el entorno virtual, debe activarse.

En **Windows**, activar el entorno virtual implica ejecutar el archivo `activate` desde la carpeta `Scripts` dentro del directorio del entorno virtual. En **Linux/Mac**, el archivo `activate` estará dentro de la carpeta `bin`.

### 3. Instalar Dependencias

Una vez activado el entorno virtual, se deben instalar los requisitos definidos en el archivo `requirements.txt`. Esto asegura que todas las dependencias necesarias para ejecutar el sistema se encuentren correctamente configuradas.

### 4. Configurar la Base de Datos

Es necesario realizar los siguientes pasos para configurar la base de datos:

1. Crear una base de datos en PostgreSQL con el nombre `cinema_db`.
2. Abrir el archivo `settings.py` del proyecto y ajustar la sección `DATABASES` con los datos de conexión de la base de datos.

Un ejemplo de configuración es el siguiente:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cinema_db',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Migrar la Base de Datos

El siguiente paso es realizar las migraciones necesarias para preparar la base de datos. Esto incluye aplicar las configuraciones de los modelos definidos en el sistema.

### 6. Ejecutar el Servidor

Para iniciar el sistema, es necesario navegar hasta el directorio donde se encuentra el archivo `manage.py` y ejecutar el servidor de desarrollo de Django. Esto permitirá acceder al sistema desde un navegador web en la dirección [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Funcionalidades Principales

- **Gestión de Películas**: Posibilidad de agregar, editar y eliminar películas del sistema.
- **Gestión de Salas**: Administración de las salas, su capacidad y los formatos compatibles.
- **Gestión de Funciones**: Creación y configuración de funciones para cada película.
- **Promociones y Tickets**: Configuración de promociones dinámicas y generación de tickets.
- **Sistema de Usuarios**: Implementación de un sistema básico de usuarios con autenticación.

## Autores

Este proyecto fue desarrollado por:

- **Viscovich Ariel**
- **Cuello Candela**
- **Taborda Vanesa**
- **Blanco Andrés**
- **Dinoto Giuliana**

