from flask import Flask, render_template, request
import sqlite3
from argon2 import PasswordHasher

app = Flask(__name__)

db = sqlite3.connect('bancodedados.db')
cursor = db.cursor()

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('userName')
        email = request.form.get('userEmail')
        password = request.form.get('userPwd')
        conf_password = request.form.get('userConfirPwd')

        if not username or not email or not password or not conf_password:
            return "Erro, campos inválidos"
        
        else:
            result = cursor.execute('SELECT ? FROM users', email)
            print(result)

        return "Conta Criada!"

    else:
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('userName')
        email = request.form.get('userEmail')

        if not username or not email:
            return "Erro, campos inválidos", 400

        else:
            result = cursor.execute('SELECT email FROM users')
            print(result)
        return "Login bem-sucedido!"
    
    else:
        return render_template("login.html")
