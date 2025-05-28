# Model/Model_GN.py

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

class Nota:
    def __init__(self, id_nota, titulo, contenido, nombre_usuario):
        self.id_nota = id_nota
        self.titulo = titulo
        self.contenido = contenido
        self.nombre_usuario = nombre_usuario
