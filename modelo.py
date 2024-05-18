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
