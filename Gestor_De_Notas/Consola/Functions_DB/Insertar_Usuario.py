import sys
sys.path.append(".")  # Para acceder correctamente al resto del proyecto

from Controller.Controller_GN import Controller_GN
from Model.Model_GN import Usuario

def insertar_usuario():
    print("\n📌 Inserción de Usuario")

    username = input("Ingrese el nombre de usuario: ").strip()
    password = input("Ingrese la contraseña: ").strip()

    # Crear instancia del modelo
    nuevo_usuario = Usuario(username=username, password=password)

    try:
        Controller_GN.insertar_usuario(nuevo_usuario)
        print(f"\n✅ Usuario '{username}' insertado correctamente.\n")
    except Exception as e:
        print(f"\n❌ Error al insertar el usuario: {e}\n")
