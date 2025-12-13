from flask import request
from flask_restx import Resource
from src.documentacion.inicio_sesion_documentacion import inicio_sesion_doc
from src.comun.utilidades import api
from flask_jwt_extended import create_access_token


class InicioSesionControlador(Resource):

    @api.expect(inicio_sesion_doc)
    def post(self):
        try:
            #obteniendo las credenciales del usuario
            usuario = request.json['usuario']
            contrasenia = request.json['contrasenia']

            #validando las credenciales
            if usuario != "test" or contrasenia != "test":
                return {"msg": "El usuario y/o la contraseñ no son correctos"}, 401

            #retornanod el token
            access_token = create_access_token(identity=usuario)
            return access_token, 200
        
        except Exception as err:
            return {"mensaje":"Algo salió mal, intentalo denuevo."},503 


