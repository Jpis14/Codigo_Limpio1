from Model.Nota import Nota

class GestorNotas:
    def __init__(self):
        self.notas = {}  # diccionario id_nota : Nota
        self.contador_id = 1  # para generar ids únicos

    def insertar_nota(self, nota: Nota):
        # Validar contenido entre 0 y 5
        if not (0 <= nota.contenido <= 5):
            raise ValueError("La nota debe estar entre 0 y 5.")
        
        # Generar id único
        id_nota = self.contador_id
        self.contador_id += 1
        
        nota.id_nota = id_nota
        self.notas[id_nota] = nota
        return id_nota

    def editar_nota(self, id_nota, nueva_nota: Nota):
        if id_nota not in self.notas:
            raise ValueError("No existe una nota con ese ID.")
        if not (0 <= nueva_nota.contenido <= 5):
            raise ValueError("La nota debe estar entre 0 y 5.")
        
        # Actualizar datos de la nota existente
        self.notas[id_nota].titulo = nueva_nota.titulo
        self.notas[id_nota].contenido = nueva_nota.contenido
        self.notas[id_nota].nombre_usuario = nueva_nota.nombre_usuario

    def eliminar_nota(self, id_nota):
        if id_nota not in self.notas:
            raise ValueError("No existe una nota con ese ID.")
        del self.notas[id_nota]

    def existe_nota(self, id_nota):
        return id_nota in self.notas

    def obtener_notas_por_usuario(self, nombre_usuario):
        return [nota for nota in self.notas.values() if nota.nombre_usuario == nombre_usuario]
