

from flask_restx import fields
from src.comun.utilidades import api


pokemon_documentacion = api.model('PokemonDocumentacionEntrada',{
    'nombre': fields.String(required=True,example='Charmander'),
    'descripcion': fields.String(required=False,example='Fuego'),
    'nivel': fields.Integer(required=False,example=1),

})