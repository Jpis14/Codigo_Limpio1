# Model/Nota.py

class Nota:
    def __init__(self, titulo, contenido, nombre_usuario, id_nota=None):
        self.id_nota = id_nota  # se asigna al insertar
        self.titulo = titulo
        self.contenido = contenido  # número entre 0 y 5
        self.nombre_usuario = nombre_usuario
