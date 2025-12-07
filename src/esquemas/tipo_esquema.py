from src.comun.utilidades import ma
from marshmallow import fields, validate
from src.modelo.tipo_modelo import TipoModelo

class TipoEsquema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TipoModelo
        load_instance = True

    codigo_tipo = fields.Integer(
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
            max=100,
            error= "El campo debe tener un tamaño entre 1 a 100 carácteres"
        ),
        error_messages ={
            "required": "El campo es obligatorio."
            }
    )

