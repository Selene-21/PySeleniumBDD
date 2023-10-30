# Proyecto Practica Python y Selenium

## Indice

- [Configuracion de Python](#Configuracion-de-Python)
- [Creacion del entorno vitual](#creacion-del-entorno-virtual)
- [Como intalar paquetes de Python](#como-instalar-paquetes-de-python)
- [Como crear un archivo Requirements.txt](#como-crear-archivo-requirementstxt)
- [Como instalar un Requirements.txt de otro repo](#como-instalar-un-archivo-requirements-de-otro-repositorio)

## Configuracion de Python

1. Instalar Python desde : http://www.python.org/downloads
2. En windows acceder a "editar variables de entorno" y agregar en PATH la ruta de los scripts dentro de la carpeta de Python

## Creacion del entorno virtual

1. Ejecutar en la terminal el comando "python -venv my-venv"
2. Realizar un "cd my-env"
3. Realizar un "cd \Scripts"
4. Realizar un "dir"
5. Ejecutar el comando "\Activate.ps1"
6. Ejecutar "cd.." tantas veces sea necesario para volver a la carpeta raíz del proyecto

## Para Ejecución de los test

1. Ejecutar el comando "python -m pytest -s -k "nombre del test"

## Como instalar paquetes de Python

1. Ejecutar el comando pip install "nombre del paquete"

## Como crear archivo Requirements.txt

1. Ejecutar el comando pip freeze > requirements.txt

## Como instalar un archivo requirements de otro repositorio

1. Ejecutar el comando pip install -r requirements.txt

## RECORDATORIOS IMPORTANTES

1. Cada vez que se realiza un "pip install package", se debe ejecutar a posteriori un "pip freeze > requirements.txt".

## Como realizar tu primer TEST

1.
