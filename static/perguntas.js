let perguntaIndex = 0;

document.getElementById('botao-adicionar-pergunta').addEventListener('click', function() {
    const container = document.getElementById('perguntas-container');
    const perguntaDiv = document.createElement('div');
    perguntaDiv.classList.add('pergunta');
    
    perguntaDiv.innerHTML = `
        <label for="texto_pergunta">Pergunta:</label>
        <input type="text" name="texto_pergunta[]" placeholder="Digite sua pergunta" required>
        
        <label for="tipo_pergunta">Tipo de Resposta:</label>
        <select name="tipo_pergunta[]" onchange="atualizarOpcoes(this, ${perguntaIndex})">
            <option value="curta">Resposta Curta</option>
            <option value="longa">Resposta Longa</option>
            <option value="multipla">Múltipla Escolha</option>
            <option value="caixa">Caixa de Seleção</option>
        </select>

        <div class="opcoes-container" id="opcoes_${perguntaIndex}" style="display: none;">
            <div class="opcao">
                <input type="text" name="opcoes_${perguntaIndex}[]" placeholder="Digite uma opção">
                <button type="button" onclick="removerOpcao(this)">Remover Opção</button>
            </div>
            <button type="button" onclick="adicionarOpcao(this, ${perguntaIndex})">Adicionar Opção</button>
        </div>

        <button type="button" onclick="removerPergunta(this)">Remover Pergunta</button>
    `;
    container.appendChild(perguntaDiv);
    perguntaIndex++; 
});


function atualizarOpcoes(selectElement, perguntaIndex) {
    const opcoesContainer = document.getElementById(`opcoes_${perguntaIndex}`);
    if (selectElement.value === 'multipla' || selectElement.value === 'caixa') {
        opcoesContainer.style.display = 'block';
    } else {
        opcoesContainer.style.display = 'none';
    }
}

function adicionarOpcao(button, perguntaIndex) {
    const opcoesContainer = button.closest('.opcoes-container');
    const opcaoDiv = document.createElement('div');
    opcaoDiv.classList.add('opcao');
    opcaoDiv.innerHTML = `
        <input type="text" name="opcoes_${perguntaIndex}[]" placeholder="Digite uma opção">
        <button type="button" onclick="removerOpcao(this)">Remover Opção</button>
    `;
    opcoesContainer.insertBefore(opcaoDiv, button);
}

function removerPergunta(button) {
    button.closest('.pergunta').remove();
}

function removerOpcao(button) {
    button.closest('.opcao').remove();
}
