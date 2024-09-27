from flask import render_template, request, redirect, url_for
from sqlalchemy.orm import joinedload
from app import app, db
from models import Formulario, Pergunta, Opcao

@app.route('/')
def index():
    formularios = Formulario.query.all()
    return render_template('pagina_inicial.html', formularios=formularios)


@app.route('/criar_formulario', methods=['GET', 'POST'])
def criar_formulario():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')

        novo_formulario = Formulario(titulo=titulo, descricao=descricao)
        db.session.add(novo_formulario)
        db.session.commit()

        textos_perguntas = request.form.getlist('texto_pergunta[]')
        tipos_perguntas = request.form.getlist('tipo_pergunta[]')

        for i, texto in enumerate(textos_perguntas):
            tipo = tipos_perguntas[i]
            
            nova_pergunta = Pergunta(
                formulario_id=novo_formulario.id,
                tipo_pergunta=tipo,
                texto_pergunta=texto
            )
            db.session.add(nova_pergunta)
            db.session.commit()

            if tipo in ['multipla', 'caixa']:
                opcoes = request.form.getlist(f'opcoes_{i}[]')
                for opcao_texto in opcoes:
                    if opcao_texto.strip():
                        nova_opcao = Opcao(
                            pergunta_id=nova_pergunta.id,
                            texto_opcao=opcao_texto
                        )
                        db.session.add(nova_opcao)
            db.session.commit()

        return redirect(url_for('index'))

    return render_template('criar_formulario.html')


@app.route('/editar_formulario/<int:formulario_id>', methods=['GET', 'POST'])
def editar_formulario(formulario_id):
    formulario = Formulario.query.get_or_404(formulario_id)
    
    if request.method == 'POST':
        formulario.titulo = request.form['titulo']
        formulario.descricao = request.form['descricao']
        submitted_question_ids = request.form.getlist('question_ids[]')
        submitted_question_ids_int = [int(qid) for qid in submitted_question_ids]
        existing_question_ids = [pergunta.id for pergunta in formulario.perguntas]
        questions_to_delete = set(existing_question_ids) - set(submitted_question_ids_int)

        for question_id in questions_to_delete:
            Opcao.query.filter_by(pergunta_id=question_id).delete()
            Pergunta.query.filter_by(id=question_id).delete()

        perguntas_textos = request.form.getlist('texto_pergunta[]')
        tipos_perguntas = request.form.getlist('tipo_pergunta[]')

        for i in range(len(perguntas_textos)):
            question_id = int(submitted_question_ids[i])
            texto_pergunta = perguntas_textos[i]
            tipo_pergunta = tipos_perguntas[i]

            if question_id > 0:
                pergunta = Pergunta.query.get(question_id)
                if pergunta:
                    pergunta.texto_pergunta = texto_pergunta
                    pergunta.tipo_pergunta = tipo_pergunta
                    Opcao.query.filter_by(pergunta_id=pergunta.id).delete()
            else:
                pergunta = Pergunta(formulario_id=formulario_id, texto_pergunta=texto_pergunta, tipo_pergunta=tipo_pergunta)
                db.session.add(pergunta)
                db.session.commit() 

            if tipo_pergunta in ['multipla', 'caixa']:
                opcoes = request.form.getlist(f'opcoes_{question_id}[]')
                for opcao_texto in opcoes:
                    nova_opcao = Opcao(pergunta_id=pergunta.id, texto_opcao=opcao_texto)
                    db.session.add(nova_opcao)

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar_formulario.html', formulario=formulario)



#exclui formulario
@app.route('/excluir_formulario/<int:formulario_id>', methods=['POST'])
def excluir_formulario(formulario_id):
    formulario = Formulario.query.get(formulario_id)
    db.session.delete(formulario)
    db.session.commit()
    return redirect(url_for('index'))

#adiciona pergunta
@app.route('/formulario/<int:formulario_id>/adicionar_pergunta', methods=['GET', 'POST'])
def adicionar_pergunta(formulario_id):
    if request.method == 'POST':
        texto_pergunta = request.form['texto_pergunta']
        tipo_pergunta = request.form['tipo_pergunta']
        
        nova_pergunta = Pergunta(formulario_id=formulario_id, tipo_pergunta=tipo_pergunta, texto_pergunta=texto_pergunta)
        db.session.add(nova_pergunta)
        db.session.commit()

        if tipo_pergunta in ['multipla', 'caixa']:
            opcoes = request.form.getlist('opcoes')
            for opcao_texto in opcoes:
                nova_opcao = Opcao(texto_opcao=opcao_texto, pergunta_id=nova_pergunta.id)
                db.session.add(nova_opcao)

        db.session.commit()
        return redirect(url_for('visualizar_formulario', formulario_id=formulario_id))
    
    return render_template('adicionar_pergunta.html', formulario_id=formulario_id)

#visualiza
@app.route('/visualizar_formulario/<int:formulario_id>', methods=['GET'])
def visualizar_formulario(formulario_id):
    formulario = Formulario.query.options(
        joinedload(Formulario.perguntas).joinedload(Pergunta.opcoes)
    ).get_or_404(formulario_id)
    
    return render_template('visualizar_formulario.html', formulario=formulario)

#exclui pergunta
@app.route('/excluir_pergunta/<int:pergunta_id>', methods=['POST'])
def excluir_pergunta(pergunta_id):
    pergunta = Pergunta.query.get(pergunta_id)
    db.session.delete(pergunta)
    db.session.commit()
    return redirect(url_for('visualizar_formulario', formulario_id=pergunta.formulario_id))
