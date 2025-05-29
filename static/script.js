document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const nome = document.querySelector('#nome').value;
        const email = document.querySelector('#email').value;
        const celular = document.querySelector('#celular').value;
        const mensagem = document.querySelector('#mensagem').value;

        const dados = { nome, email, celular, mensagem };

        try {
            const resposta = await fetch('/contato', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dados)
            });

            const resultado = await resposta.json();
            if (resposta.ok) {
                alert('Mensagem enviada com sucesso!');
                form.reset();
            } else {
                alert('Erro: ' + resultado.erro);
            }
        } catch (erro) {
            alert('Erro ao enviar mensagem.');
        }
    });
});
