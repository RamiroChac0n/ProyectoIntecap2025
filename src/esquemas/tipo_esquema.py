from src.comun.utilidades import ma
from marshmallow import fields, validate

class TipoEsquema(ma.Schema):

    codigo_tipo = fields.Integer(
        required=True,
        validate = validate.Range(min=1)
    )

    nombre = fields.String(
        required=True, 
        validate=validate.Length(min=1,max=100)
    )


class TipoEsquemaCreacion(ma.Schema):

    nombre = fields.String(
        required=True, 
        validate=validate.Length(min=1,max=100)
    )