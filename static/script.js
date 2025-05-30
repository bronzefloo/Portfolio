document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#form');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const nome = document.querySelector('#nome').value.trim();
        const email = document.querySelector('#email').value.trim();
        const celular = document.querySelector('#celular').value.trim();
        const mensagem = document.querySelector('#mensagem').value.trim();

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
                alert('Erro: ' + (resultado.erro || 'Não foi possível enviar a mensagem.'));
            }
        } catch (erro) {
            alert('Erro ao enviar mensagem.');
            console.error(erro);
        }
    });
});
