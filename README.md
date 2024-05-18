# Gestión de Usuarios con MVC en Python

Este proyecto es una aplicación de gestión de usuarios que sigue el patrón de diseño Modelo-Vista-Controlador (MVC) en Python. Permite listar y añadir usuarios almacenados en un archivo de texto.

## Autor: [DevCristobalvc](https://devcristobalvc.netlify.app/) -> cristobalvalencia3002@gmail.com

## Estructura del Proyecto

El proyecto está dividido en cuatro archivos principales:

- `modelo.py`: Contiene la lógica de negocio y las operaciones sobre los datos.
- `vista.py`: Se encarga de la presentación de los datos y la interacción con el usuario.
- `controlador.py`: Coordina las interacciones entre el modelo y la vista.
- `app.py`: Es el punto de entrada de la aplicación que proporciona un menú para interactuar con el usuario.

## Archivos

### `modelo.py`
Gestiona los datos y la lógica de negocio.

```
import os

class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class UsuarioModelo:
    def obtener_usuarios(self):
        usuarios = []
        if os.path.exists("usuarios.txt"):
            with open("usuarios.txt", "r") as archivo:
                for linea in archivo:
                    id, nombre, email = linea.strip().split(',')
                    usuarios.append(Usuario(id, nombre, email))
        return usuarios

    def guardar_usuario(self, usuario):
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{usuario.id},{usuario.nombre},{usuario.email}\n")
```

### `vista.py`
Se encarga de la presentación de los datos.

```
from modelo import Usuario

class UsuarioVista:
    def mostrar_usuarios(self, usuarios):
        for usuario in usuarios:
            print(f"ID: {usuario.id} Nombre: {usuario.nombre} Email: {usuario.email}")

    def solicitar_nuevo_usuario(self):
        id = input("Ingrese el ID: ")
        nombre = input("Ingrese el Nombre: ")
        email = input("Ingrese el Email: ")
        return Usuario(id, nombre, email)
```

### `controlador.py`
Coordina la lógica de la aplicación.

```
from modelo import UsuarioModelo, Usuario
from vista import UsuarioVista

class UsuarioControlador:
    def __init__(self):
        self.modelo = UsuarioModelo()
        self.vista = UsuarioVista()

    def listar_usuarios(self):
        usuarios = self.modelo.obtener_usuarios()
        self.vista.mostrar_usuarios(usuarios)

    def añadir_usuario(self):
        nuevo_usuario = self.vista.solicitar_nuevo_usuario()
        self.modelo.guardar_usuario(nuevo_usuario)
        print("Usuario guardado con éxito.")
```

### `app.py`
Punto de entrada de la aplicación.

```
from controlador import UsuarioControlador

class Aplicacion:
    def __init__(self):
        self.controlador = UsuarioControlador()

    def ejecutar(self):
        while True:
            print("1. Listar usuarios")
            print("2. Añadir usuario")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.controlador.listar_usuarios()
            elif opcion == "2":
                self.controlador.añadir_usuario()
            elif opcion == "3":
                break

if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()
```

## Uso

1. Asegúrate de que los archivos `modelo.py`, `vista.py`, `controlador.py`, y `app.py` estén en el mismo directorio.
2. Ejecuta el archivo `app.py` con Python:

```
python app.py
```

3. Sigue las instrucciones en pantalla para listar usuarios o añadir un nuevo usuario.

## Requisitos

- [Python 3.12.3](https://www.python.org/downloads/)

## Notas

- El archivo `usuarios.txt` se creará automáticamente en el mismo directorio si no existe.
- Los datos de los usuarios se almacenan en el archivo `usuarios.txt` en formato CSV (`id,nombre,email`).

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.
