from UI.interfaz import iniciar_interfaz
from Model.Start_Consola import Start_Consola


if __name__ == "__main__":
    modo = input("¿Usar interfaz gráfica (g) o consola (c)? ").strip().lower()
    if modo == 'g':
        iniciar_interfaz()
    elif modo == 'c':
        #Inicio de Consola
        if __name__ == "__main__":
            start = Start_Consola()
            start.start()
    else:
        print("Opción no válida.")
