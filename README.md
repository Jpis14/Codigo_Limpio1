# Gestor de Notas
## ¿Quién hizo esto?
**Autor**:
- Juan Pablo Hernandez Huertas
  
## ¿Qué es y para qué es?
Este proyecto permite a los usuarios (registrarse, iniciar sesión y gestionar notas) de manera eficiente.  

### Características  
- Registro e inicio de sesión de usuarios.  
- Creación, edición y eliminación de notas.  
- Validación de datos para mayor seguridad.  
- Pruebas unitarias para asegurar el correcto funcionamiento.
- Interfaz de consola.
- Interfaz grafica, amigable con el usuario.
- Interfaz web, con estilo sencillo, pero optimizado. 

### Prerrequisitos
Asegurese de tener `Python` instalado en su sistema. Ademas de también añadir `pytest` que es el encargado de correr las pruebas unitarias, así como también debe añadir `tkinter` que es el encargado de procesar la interfaz de usuario.<br>Por otro lado, tambien es necesario tener e el sistema las librerias `psycopg2` y `flask`, las cuales son necesarias para conectarse y trabajar con bases de datos PostgreSQL y para crear aplicaciones web de forma sencilla y rápida.<br> <br> Para acceder a la base de datos es necesesario estar logueado en:
```bash
https://console.neon.tech/
```
Para luego crear un nuevo proyecto y conectarlo con la base de datos dandole click en el boton `Connect to your database` y copiando las credenciales como: `Parameters only`. Para luego ser ubicadas en el archivo `Secret_Config.py`, que es el modulo necesario para el enlace con la base de datos, donde se encuentran las credenciales de `Neon_DB`, teniendo en cuenta que NO se debe eliminar la variable `PGPORT=5432` que se utiliza para indicar el puerto en el que el servidor de PostgreSQL está escuchando las conexiones.<br> Este archivo esta ubicado en:
```bash
Gestor_De_Notas/Secret_Config.py
```

## Ejecución
### Pruebas

1. Para correr las pruebas debes tener pytest una libreria de python
2. Debes el ejecutar el archivo `GestorPruebas.py` ubicado en la ruta:
```bash
Gestor_De_Notas/Pruebas/GestorPruebas.py
```

### Arranque de aplicaciones

* Para ejecutar la consola debe ejecutar el archivo `Consola_Def.py` ubicado en la ruta:
```bash
Gestor_De_Notas/Consola/Consola_Def.py
```
* Para ejecutar la interfaz grafica debe ejecutar el archivo `interfaz.py` ubicado en la ruta:
```bash
Gestor_De_Notas/UI/interfaz.py
```
* Para ejecutar la interfaz web debe ejecutar el archivo `app.py` ubicado en la ruta:
```bash
Gestor_De_Notas/app.py
```
    
### Dependencias
- `pytest`: Librería estándar de Python para pruebas unitarias.
- `tkinter`: Librería de Python para el desarrollo de interfaces gráficas.
- `psycopg2`: es una librería de Python que permite conectarse y trabajar con bases de datos PostgreSQL.
- `flask`: es una librería de Python para crear aplicaciones web de forma sencilla y rápida.
  

