import psycopg2
import SecretConfig

class Controller_GN:

    @staticmethod
    def ObtenerCursor():
        connection = psycopg2.connect(
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD,
            host=SecretConfig.PGHOST,
            port=SecretConfig.PGPORT
        )
        return connection.cursor()

    @staticmethod
    def CrearTablas():
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuario (
                nombre_usuario VARCHAR(50) PRIMARY KEY,
                contrasena VARCHAR(50) NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nota (
                id_nota SERIAL PRIMARY KEY,
                titulo VARCHAR(100),
                contenido FLOAT CHECK (contenido >= 0 AND contenido <= 5),
                nombre_usuario VARCHAR(50),
                FOREIGN KEY (nombre_usuario) REFERENCES usuario(nombre_usuario)
            );
        """)
        cursor.connection.commit()

    @staticmethod
    def EliminarTablas():
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("DROP TABLE IF EXISTS nota;")
        cursor.execute("DROP TABLE IF EXISTS usuario;")
        cursor.connection.commit()

    @staticmethod
    def InsertarUsuario(usuario):
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = %s", (usuario.nombre_usuario,))
        if cursor.fetchone():
            raise Exception("El usuario ya existe.")
        cursor.execute("INSERT INTO usuario (nombre_usuario, contrasena) VALUES (%s, %s)",
                       (usuario.nombre_usuario, usuario.contrasena))
        cursor.connection.commit()

    @staticmethod
    def BuscarUsuario(nombre_usuario):
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT nombre_usuario, contrasena FROM usuario WHERE nombre_usuario = %s", (nombre_usuario,))
        fila = cursor.fetchone()
        if not fila:
            raise Exception("Usuario no encontrado.")
        from Model.Model_GN import Usuario
        return Usuario(fila[0], fila[1])

    @staticmethod
    def ActualizarUsuario(nombre_usuario, nueva_contrasena):
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT * FROM usuario WHERE nombre_usuario = %s", (nombre_usuario,))
        if not cursor.fetchone():
            raise Exception("El usuario no existe.")
        cursor.execute("UPDATE usuario SET contrasena = %s WHERE nombre_usuario = %s",
                       (nueva_contrasena, nombre_usuario))
        cursor.connection.commit()

    @staticmethod
    def InsertarNota(nota):
        try:
            cursor = Controller_GN.ObtenerCursor()
            contenido = str(nota.contenido).replace(',', '.')
            valor = float(contenido)
            if not (0 <= valor <= 5):
                raise Exception("El contenido debe estar entre 0.0 y 5.0")

            cursor.execute("""
                INSERT INTO nota (titulo, contenido, nombre_usuario)
                VALUES (%s, %s, %s)
                RETURNING id_nota;
            """, (nota.titulo, valor, nota.nombre_usuario))

            id_generado = cursor.fetchone()[0]
            cursor.connection.commit()
            return id_generado
        except Exception as e:
            raise Exception(f"Error al insertar nota: {e}")

    @staticmethod
    def EditarNota(id_nota, nueva_nota):
        if not Controller_GN.ExisteNota(id_nota):
            raise Exception("No existe una nota con ese ID")

        try:
            valor = float(str(nueva_nota.contenido).replace(",", "."))
            if not (0 <= valor <= 5):
                raise Exception("El contenido debe estar entre 0 y 5.")
        except ValueError:
            raise Exception("Contenido inválido. Debe ser un número entre 0 y 5.")

        cursor = Controller_GN.ObtenerCursor()
        cursor.execute(
            "UPDATE nota SET titulo = %s, contenido = %s WHERE id_nota = %s",
            (nueva_nota.titulo, valor, id_nota)
        )
        cursor.connection.commit()

    @staticmethod
    def EliminarNota(id_nota):
        if not Controller_GN.ExisteNota(id_nota):
            raise Exception("No existe una nota con ese ID")

        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("DELETE FROM nota WHERE id_nota = %s", (id_nota,))
        cursor.connection.commit()

    @staticmethod
    def ExisteNota(id_nota):
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT * FROM nota WHERE id_nota = %s", (id_nota,))
        return cursor.fetchone() is not None

    @staticmethod
    def BuscarNotasPorUsuario(nombre_usuario):
        cursor = Controller_GN.ObtenerCursor()
        cursor.execute("SELECT id_nota, titulo, contenido FROM nota WHERE nombre_usuario = %s", (nombre_usuario,))
        notas = cursor.fetchall()
        return notas

