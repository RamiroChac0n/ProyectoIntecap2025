

from flask_restx import fields
from src.comun.utilidades import api


pokemon_x_tipo_documentacion = api.model('PokemonXTipoDocumentacionEntrada',{
    'codigo_tipo': fields.Integer(required=True,example=1),
    'codigo_pokemon': fields.Integer(required=True,example=1),
})