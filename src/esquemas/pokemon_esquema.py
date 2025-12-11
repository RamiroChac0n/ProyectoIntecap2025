from src.comun.utilidades import ma
from marshmallow import fields, validate
from src.modelo.pokemon_modelo import PokemonModelo

class PokemonEsquema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PokemonModelo
        load_instance = True

    codigo_pokemon = fields.Integer(
        required=True,
        validate = validate.Range(min=1),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    nombre = fields.String(
        required=True, 
        validate=validate.Length(
            min=1,
            max=200,
            error= "El campo debe tener un tamaño entre 1 a 200 carácteres"
        ),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    descripcion = fields.String(
        required=False, 
        validate=validate.Length(
            min=1,
            error= "El campo debe tener minímo 1 caracter"
        ),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    nivel = fields.Integer(
        required=False,
        validate = validate.Range(min=1),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

    

