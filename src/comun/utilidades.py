#cargar librerias para la documentacion, bases de datos y jwt
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_marshmallow import Marshmallow

db = SQLAlchemy()

api = Api()

ma = Marshmallow()