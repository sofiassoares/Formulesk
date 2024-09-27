import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://user:password@host/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

