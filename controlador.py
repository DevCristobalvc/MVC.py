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
