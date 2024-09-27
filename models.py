from app import db

class Formulario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    perguntas = db.relationship('Pergunta', backref='formulario', lazy=True, cascade="all, delete")

class Pergunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formulario_id = db.Column(db.Integer, db.ForeignKey('formulario.id'), nullable=False)
    tipo_pergunta = db.Column(db.String(50), nullable=False)
    texto_pergunta = db.Column(db.Text, nullable=False)
    opcoes = db.relationship('Opcao', backref='pergunta', lazy=True, cascade="all, delete")

class Opcao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto_opcao = db.Column(db.String(200), nullable=False)
    pergunta_id = db.Column(db.Integer, db.ForeignKey('pergunta.id'), nullable=False)
