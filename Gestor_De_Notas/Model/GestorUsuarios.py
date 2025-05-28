from Model.Validar import Validar
from Model.Usuario import Usuario
from Controller.Controller_GN import Controller_GN

class GestorUsuarios:
    def __init__(self):
        self.validar = Validar()

    def registrar_usuario(self):
        nombre = self.validar.validar_entrada("Ingrese nombre de usuario: ", "usuario")
        contrasena = self.validar.validar_entrada("Ingrese contraseña: ", "contraseña")
        try:
            usuario = Usuario(nombre, contrasena)
            Controller_GN.InsertarUsuario(usuario)
            print("✅ Usuario registrado correctamente.")
            return usuario
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
            return None

    def iniciar_sesion(self):
        nombre = self.validar.validar_entrada("Ingrese nombre de usuario: ", "usuario")
        contrasena = self.validar.validar_entrada("Ingrese contraseña: ", "contraseña")
        try:
            usuario = Controller_GN.BuscarUsuario(nombre)
            if usuario.contrasena == contrasena:
                print(f"✅ Bienvenido, {nombre}.")
                return usuario
            else:
                print("❌ Contraseña incorrecta.")
                return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None

    def cambiar_contrasena(self, usuario):
        nueva_contra = self.validar.validar_entrada("Ingrese nueva contraseña: ", "contraseña")
        try:
            Controller_GN.ActualizarUsuario(usuario.nombre_usuario, nueva_contra)
            usuario.contrasena = nueva_contra
            print("✅ Contraseña actualizada con éxito.")
        except Exception as e:
            print(f"❌ Error al actualizar contraseña: {e}")

    # Métodos para la interfaz gráfica, sin inputs por consola

    def registrar_usuario_interfaz(self, nombre, contrasena):
        try:
            usuario = Usuario(nombre, contrasena)
            Controller_GN.InsertarUsuario(usuario)
            return True
        except Exception:
            return False

    def iniciar_sesion_interfaz(self, nombre, contrasena):
        try:
            usuario = Controller_GN.BuscarUsuario(nombre)
            if usuario.contrasena == contrasena:
                return usuario
            return None
        except Exception:
            return None

    def cambiar_contrasena_interfaz(self, usuario, nueva_contrasena):
        try:
            Controller_GN.ActualizarUsuario(usuario.nombre_usuario, nueva_contrasena)
            usuario.contrasena = nueva_contrasena
            return True
        except Exception:
            return False
