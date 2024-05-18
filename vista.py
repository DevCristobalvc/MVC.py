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
