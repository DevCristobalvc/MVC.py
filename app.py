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
