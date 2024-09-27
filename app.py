from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    with app.app_context():
        os.environ["FLASK_ENV"] = "development"
        app.run(debug=True)