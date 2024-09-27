function toggleOptions(select) {
    const perguntaDiv = select.closest('.pergunta');
    const opcoesContainer = perguntaDiv.querySelector('.opcoes-container');
    if (select.value === 'multipla' || select.value === 'caixa') {
        opcoesContainer.style.display = 'block';
    } else {
        opcoesContainer.style.display = 'none';
    }
}

let tempQuestionId = -1;

document.getElementById('add-pergunta').addEventListener('click', function() {
    const container = document.getElementById('perguntas-container');

    const perguntaDiv = document.createElement('div');
    perguntaDiv.classList.add('pergunta');
    perguntaDiv.setAttribute('data-id', tempQuestionId);

    perguntaDiv.innerHTML = `
        <input type="hidden" name="question_ids[]" value="${tempQuestionId}">
        <label>Pergunta:</label>
        <input type="text" name="texto_pergunta[]" placeholder="Digite a pergunta" required>
        
        <label>Tipo de Resposta:</label>
        <select name="tipo_pergunta[]" onchange="toggleOptions(this)">
            <option value="curta">Resposta Curta</option>
            <option value="longa">Resposta Longa</option>
            <option value="multipla">Múltipla Escolha</option>
            <option value="caixa">Caixa de Seleção</option>
        </select>

        <div class="opcoes-container" style="display: none;">
            <h4>Opções</h4>
            <button type="button" class="add-opcao">Adicionar Opção</button>
        </div>

        <button type="button" class="remover-pergunta">Remover Pergunta</button>
    `;

    container.appendChild(perguntaDiv);
    tempQuestionId--;
});

document.getElementById('perguntas-container').addEventListener('click', function(event) {
    const target = event.target;

    if (target.classList.contains('add-opcao')) {
        const opcoesContainer = target.closest('.opcoes-container');
        const perguntaDiv = opcoesContainer.closest('.pergunta');
        const questionId = perguntaDiv.getAttribute('data-id');

        const opcaoDiv = document.createElement('div');
        opcaoDiv.classList.add('opcao');
        opcaoDiv.innerHTML = `
            <input type="text" name="opcoes_${questionId}[]" placeholder="Digite uma opção" required>
            <button type="button" class="remove-option">Remover Opção</button>
        `;
        opcoesContainer.insertBefore(opcaoDiv, target);
    }

    if (target.classList.contains('remove-option')) {
        target.closest('.opcao').remove();
    }

    if (target.classList.contains('remover-pergunta')) {
        target.closest('.pergunta').remove();
    }
});

document.getElementById('editar-form').addEventListener('submit', function(event) {
});
