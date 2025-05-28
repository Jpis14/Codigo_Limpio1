import sys
sys.path.append(".")
sys.path.append("Gestor_De_Notas")

from Controller.Controller_GN import Controller_GN
from Model.Model_GN import Usuario, Nota


usuario_actual = None
Controller_GN.CrearTablas()


def mostrar_menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Actualizar contraseña")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            actualizar_contrasena()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
    contrasena = input("Ingrese la contraseña: ").strip()

    usuario = Usuario(nombre_usuario, contrasena)

    try:
        Controller_GN.InsertarUsuario(usuario)
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print(f"Error: {e}")

def iniciar_sesion():
    global usuario_actual
    print("\n--- INICIAR SESIÓN ---")
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
    contrasena = input("Ingrese la contraseña: ").strip()

    try:
        usuario = Controller_GN.BuscarUsuario(nombre_usuario)
        if usuario.contrasena == contrasena:
            print("Inicio de sesión exitoso.")
            usuario_actual = usuario
            mostrar_menu_notas()
        else:
            print("Contraseña incorrecta.")
    except Exception:
        print("Usuario no registrado.")

def actualizar_contrasena():
    print("\n--- ACTUALIZAR CONTRASEÑA ---")
    nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
    nueva_contrasena = input("Ingrese la nueva contraseña: ").strip()

    try:
        Controller_GN.ActualizarUsuario(nombre_usuario, nueva_contrasena)
        print("Contraseña actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar contraseña: {e}")

def mostrar_menu_notas():
    while True:
        print("\n--- MENÚ DE NOTAS ---")
        print("1. Crear nota")
        print("2. Eliminar nota")
        print("3. Editar nota")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_nota()
        elif opcion == "2":
            eliminar_nota()
        elif opcion == "3":
            editar_nota()
        elif opcion == "4":
            print("Cerrando sesión...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

def crear_nota():
    print("\n--- CREAR NOTA ---")
    titulo = input("Título: ").strip()
    contenido = input("Contenido (número entre 0.0 y 5.0): ").strip()

    if not es_numero_valido(contenido):
        print("El contenido debe ser un número entre 0.0 y 5.0")
        return

    contenido = contenido.replace(',', '.')

    nota = Nota(None, titulo, contenido, usuario_actual.nombre_usuario)

    try:
        id_generado = Controller_GN.InsertarNota(nota)
        print(f"Nota creada exitosamente. ID de la nota: {id_generado}")
    except Exception as e:
        print(f"Error al crear nota: {e}")

def es_numero_valido(valor):
    try:
        valor = valor.replace(',', '.')
        numero = float(valor)
        return 0 <= numero <= 5
    except ValueError:
        return False

def eliminar_nota():
    print("\n--- ELIMINAR NOTA ---")
    id_nota = input("ID de la nota a eliminar: ").strip()
    if not id_nota.isdigit():
        print("ID inválido.")
        return

    try:
        id_nota_int = int(id_nota)
        if Controller_GN.ExisteNota(id_nota_int):
            Controller_GN.EliminarNota(id_nota_int)
            print(f"Nota con ID {id_nota} eliminada correctamente.")
        else:
            print(f"No existe una nota con ID {id_nota}.")
    except Exception as e:
        print(f"Error al eliminar nota: {e}")

def editar_nota():
    print("\n--- EDITAR NOTA ---")
    id_nota = input("ID de la nota a editar: ").strip()
    if not id_nota.isdigit():
        print("ID inválido.")
        return

    nuevo_titulo = input("Nuevo título: ").strip()
    nuevo_contenido = input("Nuevo contenido (número entre 0.0 y 5.0): ").strip()

    if not es_numero_valido(nuevo_contenido):
        print("El contenido debe ser un número entre 0.0 y 5.0")
        return

    nuevo_contenido = nuevo_contenido.replace(',', '.')

    try:
        id_nota_int = int(id_nota)
        if Controller_GN.ExisteNota(id_nota_int):
            nueva_nota = Nota(id_nota_int, nuevo_titulo, nuevo_contenido, usuario_actual.nombre_usuario)
            Controller_GN.EditarNota(id_nota_int, nueva_nota)
            print(f"Nota con ID {id_nota} actualizada correctamente.")
        else:
            print(f"No existe una nota con ID {id_nota}.")
    except Exception as e:
        print(f"Error al actualizar nota: {e}")

if __name__ == "__main__":
    mostrar_menu_principal()
