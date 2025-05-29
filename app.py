from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form.get('nome')
    email = request.form.get('email')
    celular = request.form.get('celular')
    mensagem = request.form.get('mensagem')

    try:
        with open('mensagens.txt', 'a', encoding='utf-8') as f:
            f.write(f'Nome: {nome}\nEmail: {email}\nCelular: {celular}\nMensagem: {mensagem}\n---\n')
        return "Enviado com sucesso", 200
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
