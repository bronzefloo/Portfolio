from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Troque por uma chave forte!

# Configurações do e-mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # Seu e-mail
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')  # Senha de app via variável de ambiente

mail = Mail(app)

DB_PATH = 'contatos.db'

def criar_tabela():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                celular TEXT,
                mensagem TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    criar_tabela()
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        celular = request.form.get('celular', '')
        mensagem = request.form['mensagem']

        # Salvar no banco
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contatos (nome, email, celular, mensagem) VALUES (?, ?, ?, ?)',
                    (nome, email, celular, mensagem))
        conn.commit()
        conn.close()

        # Enviar e-mail
        try:
            msg = Message('Novo contato pelo site',
                        sender=app.config['MAIL_USERNAME'],
                        recipients=[app.config['MAIL_USERNAME']])
            msg.body = f"Nome: {nome}\nEmail: {email}\nCelular: {celular}\nMensagem:\n{mensagem}"
            mail.send(msg)
            flash('Mensagem enviada com sucesso!')
        except Exception as e:
            flash('Erro ao enviar e-mail. Verifique a configuração ou tente novamente.')
            print(f'Erro no envio de e-mail: {e}')

        return redirect(url_for('index') + '#contato')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
