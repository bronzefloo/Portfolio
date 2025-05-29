from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    celular = dados.get('celular')
    mensagem = dados.get('mensagem')

    try:
        with open('mensagens.txt', 'a', encoding='utf-8') as f:
            f.write(f'Nome: {nome}\nEmail: {email}\nCelular: {celular}\nMensagem: {mensagem}\n---\n')
        return jsonify({'mensagem': 'Enviado com sucesso'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
