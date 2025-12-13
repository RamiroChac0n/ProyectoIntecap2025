



from flask_restx import fields
from src.comun.utilidades import api


inicio_sesion_doc = api.model('InicioSesionDoc',{
    'usuario': fields.String(required=True,example='test'),
    'contrasenia': fields.String(required=True,example='test'),
})