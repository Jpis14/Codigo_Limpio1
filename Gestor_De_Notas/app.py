from flask import Flask, render_template, request, redirect, url_for, flash, session
from Controller import Controller_GN
from Model.Model_GN import Usuario
from Model.Model_GN import Nota
from functools import wraps

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'  # Cámbiala en producción

# Decorador para rutas protegidas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            flash("Por favor inicia sesión primero.", "error")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Registro de usuario
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        contraseña = request.form.get('contraseña', '').strip()
        if not nombre or not contraseña:
            flash("Por favor completa todos los campos.", "error")
            return render_template('register.html')
        try:
            nuevo_usuario = Usuario(nombre, contraseña)
            Controller_GN.Controller_GN.InsertarUsuario(nuevo_usuario)
            flash("Usuario registrado correctamente. Ahora puedes iniciar sesión.", "success")
            return redirect(url_for('login'))
        except Exception as e:
            flash(str(e), "error")
    return render_template('register.html')

# Inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        contraseña = request.form.get('contraseña', '').strip()
        if not nombre or not contraseña:
            flash("Por favor completa todos los campos.", "error")
            return render_template('login.html')
        try:
            usuario = Controller_GN.Controller_GN.BuscarUsuario(nombre)
            if usuario.contrasena == contraseña:
                session['usuario'] = usuario.nombre_usuario
                flash("Inicio de sesión exitoso.", "success")
                return redirect(url_for('menu_usuario'))
            else:
                flash("Contraseña incorrecta.", "error")
        except Exception as e:
            flash(str(e), "error")
    return render_template('login.html')

# Cambiar contraseña
@app.route('/update_password', methods=['GET', 'POST'])
def update_password():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        nueva_contraseña = request.form.get('nueva_contraseña', '').strip()
        if not nombre or not nueva_contraseña:
            flash("Por favor completa todos los campos.", "error")
            return render_template('update_password.html')
        try:
            Controller_GN.Controller_GN.ActualizarUsuario(nombre, nueva_contraseña)
            flash("La contraseña se actualizó correctamente.", "success")
        except Exception as e:
            flash(str(e), "error")
    return render_template('update_password.html')

# Menú del usuario (requiere login)
@app.route('/menu_usuario')
@login_required
def menu_usuario():
    return render_template('menu_usuario.html', usuario=session['usuario'])

# Cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for('index'))

@app.route('/notas/insertar', methods=['GET', 'POST'])
@login_required
def insertar_nota():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        contenido = request.form.get('contenido', '').strip()
        if not titulo or not contenido:
            flash("Por favor completa todos los campos.", "error")
            return render_template('insertar_nota.html')
        try:
            valor = float(contenido.replace(',', '.'))
            if valor < 0 or valor > 5:
                flash("El contenido debe ser un número entre 0.0 y 5.0.", "error")
                return render_template('insertar_nota.html')

            usuario = session['usuario']
            nueva_nota = Nota(None, titulo, contenido, usuario)
            Controller_GN.Controller_GN.InsertarNota(nueva_nota)
            flash("Nota insertada correctamente.", "success")
            return redirect(url_for('menu_usuario'))
        except ValueError:
            flash("El contenido debe ser un número válido.", "error")
        except Exception as e:
            flash(str(e), "error")
        return render_template('insertar_nota.html')

    return render_template('insertar_nota.html')


@app.route('/notas/editar', methods=['GET', 'POST'])
@login_required
def editar_nota():
    if request.method == 'POST':
        id_nota = request.form.get('id_nota', '').strip()
        titulo = request.form.get('titulo', '').strip()
        contenido = request.form.get('contenido', '').strip()

        if not id_nota or not titulo or not contenido:
            flash("Por favor completa todos los campos.", "error")
            return render_template('editar_nota.html')

        try:
            id_nota_int = int(id_nota)
            valor = float(contenido.replace(',', '.'))
            if valor < 0 or valor > 5:
                flash("El contenido debe ser un número entre 0.0 y 5.0.", "error")
                return render_template('editar_nota.html')

            usuario = session['usuario']
            nueva_nota = Nota(id_nota_int, titulo, contenido, usuario)
            Controller_GN.Controller_GN.EditarNota(id_nota_int, nueva_nota)
            flash("Nota actualizada correctamente.", "success")
            return redirect(url_for('menu_usuario'))
        except ValueError:
            flash("ID y contenido deben ser valores numéricos válidos.", "error")
        except Exception as e:
            flash(str(e), "error")

        return render_template('editar_nota.html')

    return render_template('editar_nota.html')


@app.route('/notas/eliminar', methods=['GET', 'POST'])
@login_required
def eliminar_nota():
    if request.method == 'POST':
        id_nota = request.form.get('id_nota', '').strip()

        if not id_nota:
            flash("Por favor proporciona el ID de la nota.", "error")
            return render_template('eliminar_nota.html')

        try:
            id_nota_int = int(id_nota)
            Controller_GN.Controller_GN.EliminarNota(id_nota_int)
            flash("Nota eliminada correctamente.", "success")
            return redirect(url_for('menu_usuario'))
        except ValueError:
            flash("El ID debe ser un número válido.", "error")
        except Exception as e:
            flash(str(e), "error")

        return render_template('eliminar_nota.html')

    return render_template('eliminar_nota.html')

@app.route('/notas/ver')
@login_required
def ver_notas():
    usuario = session['usuario']
    try:
        notas = Controller_GN.Controller_GN.BuscarNotasPorUsuario(usuario)
    except Exception as e:
        flash(str(e), "error")
        notas = []

    return render_template('ver_notas.html', notas=notas)


# Ejecutar app
if __name__ == '__main__':
    # Asegúrate de crear las tablas al iniciar si no existen
    try:
        Controller_GN.Controller_GN.CrearTablas()
    except Exception as e:
        print("Error al crear tablas:", e)

    app.run(debug=True)
