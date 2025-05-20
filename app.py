from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def criar_banco():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_banco()

@app.route('/')
def formulario():
    return render_template('Login.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    email = request.form['email']
    senha = request.form['senha']
    if not email or not senha:
        return "Preencha todos os campos!"

    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    hashed_senha = senha  # ou use hashing, se desejar
    cursor.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (email, hashed_senha)) 
    conn.commit()
    conn.close()

    return redirect(url_for('sucesso'))

@app.route('/Cadastro.html')
def cadastro():
    return render_template('Cadastro.html')

@app.route('/sucesso')
def sucesso():
    return render_template('Sucesso.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/EsqueciSenha.html')
def esqueci_senha():
    return render_template('EsqueciSenha.html')

if __name__ == '__main__':
    print("⚙️ Iniciando o Flask...")
    app.run(debug=True)