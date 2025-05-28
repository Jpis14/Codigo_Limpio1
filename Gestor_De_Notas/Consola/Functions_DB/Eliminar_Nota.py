import sys
sys.path.append(".")  # Acceso a módulos del proyecto

from Controller.Controller_GN import Controller_GN

def eliminar_nota():
    print("\n🗑️ Eliminación de Nota")

    usuario = input("Ingrese el nombre de usuario de la nota: ").strip()
    titulo = input("Ingrese el título de la nota a eliminar: ").strip()

    try:
        Controller_GN.eliminar_nota(usuario, titulo)
        print(f"\n✅ Nota '{titulo}' eliminada correctamente.\n")
    except Exception as e:
        print(f"\n❌ Error al eliminar la nota: {e}\n")
