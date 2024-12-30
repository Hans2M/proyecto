from flask import Flask, render_template, redirect, request, url_for, session, jsonify, send_from_directory
import random
import os

# Inicializar Flask
app = Flask(__name__)
app.secret_key = 'clave_secreta_segura'  # Cambia esto por una clave más segura

# Contraseña de acceso
PASSWORD = "r2GDj9q3"

# Variables globales
songs = ['music.mp3']
current_song = random.choice(songs)

# Poemas
poems = [
    "Eres la luz que ilumina mi camino.",
    "Tu sonrisa es mi razón de ser.",
    "En cada latido, susurra tu nombre."
]

# Ruta de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Contraseña incorrecta')
    return render_template('login.html')

# Ruta principal protegida
@app.route('/')
def index():
    if 'logged_in' in session and session['logged_in']:
        return render_template('index.html')
    return redirect(url_for('login'))

# Cerrar sesión
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

# Ruta para cambiar música
@app.route('/change-music')
def change_music():
    global current_song
    current_song = random.choice(songs)
    return jsonify({"song": f"/static/{current_song}"})

# Ruta para mostrar poema
@app.route('/get-poem')
def get_poem():
    poem = random.choice(poems)
    return jsonify({"poem": poem})

# Ruta para mostrar mensaje
@app.route('/get-message')
def get_message():
    return jsonify({"message": "Eres la persona más especial para mí. ¡Te amo!"})

# Ruta para imágenes
@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
