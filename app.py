from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    mensagem = None

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        celular = request.form.get('celular')
        msg = request.form.get('mensagem')

        try:
            with open('mensagens.txt', 'a', encoding='utf-8') as f:
                f.write(f'Nome: {nome}\nEmail: {email}\nCelular: {celular}\nMensagem: {msg}\n---\n')
            mensagem = "Obrigada, entraremos em contato!"
        except Exception as e:
            mensagem = f"Erro ao enviar: {str(e)}"

    return render_template('index.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
