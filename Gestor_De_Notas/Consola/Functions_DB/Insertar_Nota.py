import sys
sys.path.append(".")  # Acceso a módulos del proyecto

from Controller.Controller_GN import Controller_GN
from Model.Model_GN import Nota

def insertar_nota():
    print("\n📝 Inserción de Nota")

    usuario = input("Ingrese el nombre de usuario: ").strip()
    titulo = input("Ingrese el título de la nota: ").strip()
    contenido = input("Ingrese el contenido de la nota: ").strip()

    nueva_nota = Nota(usuario=usuario, titulo=titulo, contenido=contenido)

    try:
        Controller_GN.insertar_nota(nueva_nota)
        print(f"\n✅ Nota insertada correctamente para el usuario '{usuario}'.\n")
    except Exception as e:
        print(f"\n❌ Error al insertar la nota: {e}\n")
