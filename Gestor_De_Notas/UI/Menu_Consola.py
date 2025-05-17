# Menú principal
class Menu_Consola:
  @staticmethod
  def menu():
    print("\n📌 --- Menú ---")
    print("1️⃣ Crear nota")
    print("2️⃣ Editar nota")
    print("3️⃣ Eliminar nota")
    print("4️⃣ Ver todas las notas")
    print("5️⃣ Cambiar contraseña")
    print("6️⃣ Cerrar sesión")
    return input("Seleccione una opción: ")
  
