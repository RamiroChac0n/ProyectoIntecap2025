from src.comun.utilidades import ma
from marshmallow import fields, validate
from src.modelo.pokemon_x_tipo_modelo import PokemonXTipoModelo

class PokemonXTipoEsquema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PokemonXTipoModelo
        load_instance = True
        include_fk = True

    codigo_pokemon = fields.Integer(
        required=True,
        validate = validate.Range(min=1),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    codigo_tipo = fields.Integer(
        required=True,
        validate = validate.Range(min=1),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    

