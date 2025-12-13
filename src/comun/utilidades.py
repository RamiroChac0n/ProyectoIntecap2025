#cargar librerias para la documentacion, bases de datos y jwt
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()


authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Ingresa el token ingresado primero Bearer, e.g., "Bearer <token>"'
    }
}

api = Api(authorizations=authorizations,prefix="/api/v1",security="Bearer")


ma = Marshmallow()


jwt = JWTManager()