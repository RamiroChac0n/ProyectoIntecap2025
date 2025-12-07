from flask import request
from flask_restx import Resource
from src.comun.utilidades import db
from src.modelo.tipo_modelo import TipoModelo
from sqlalchemy.orm.exc import NoResultFound
from src.esquemas.tipo_esquema import TipoEsquema, TipoEsquemaCreacion
from src.comun.utilidades import api
from src.documentacion.tipo_documentacion import tipo_documentacion
from marshmallow import ValidationError


#eliminacion y busqueda por tipo por su codigo tipo
class TipoControladorPorCodigoTipo(Resource):

    #select * from table condicion
    def get(self, codigo_tipo:int):
        try:
            #buscar el elemento a ver si existe
            tipo_db = db.session.execute(db.select(TipoModelo).where(TipoModelo.codigo_tipo == codigo_tipo)).scalar_one()

            #objeto de esquema
            tipo_esquema = TipoEsquema()

            return tipo_esquema.dump(tipo_db),200

        except NoResultFound as err:
            print(err)
            return {"mensaje":"No existe el tipo que quiere consultar"},404

        except Exception as err:
            print(err)
            #excepcion general
            return {"mensaje":"Algo salió mal, intentalo denuevo."},503 
            


    #delete from tabla condicion
    def delete(self, codigo_tipo:int):
        try:
            #buscar el elemento a ver si existe
            tipo_db = db.session.execute(db.select(TipoModelo).where(TipoModelo.codigo_tipo == codigo_tipo)).scalar_one()

            #elimianr el recurso
            db.session.delete(tipo_db)
            #confirmar
            db.session.commit()

            return True,204


        except NoResultFound as err:
            print(err)
            return {"mensaje":"No existe el tipo que quieres eliminar"},404

        except Exception as err:
            print(err)
            #excepcion general
            return {"mensaje":"Algo salió mal, intentalo denuevo."},503 
            

class TipoControlador(Resource):

    #Read
    def get(self):
        #select * from pokemon
        tipos = db.session.execute(
            db.select(TipoModelo)
                                   ).scalars().all()
        print(tipos)
        return {'respuesta':'busqueda'},200
    
    #Create
    @api.expect(tipo_documentacion)
    def post(self):
        try:
            #crear tipo
            tipo_json = request.json

            #validar reglas
            tipo_esquema = TipoEsquemaCreacion()
            tipo_validado = tipo_esquema.load(tipo_json)

            tipo = TipoModelo(nombre=tipo_validado['nombre'])
            db.session.add(tipo)
            db.session.commit()

            #objeto de esquema
            tipo_esquema = TipoEsquema()

            return tipo_esquema.dump(tipo),200
        except ValidationError as err:
            print(err)
            return {"mensaje":"No se pudo insertar porque no envio todos los campos de manera correcta"},422
        except Exception as err:
            print(err)
            return {"mensaje":"Algo salió mal, intentalo denuevo."},503 
        
    
    #Update
    def put(self):
        #objeto y lo validar
        #select * from TipoModelo where = 1
        tipo_db = db.session.execute(db.select(TipoModelo).where(TipoModelo.codigo_tipo == 1)).scalar_one()
        tipo_db.nombre = "Super fuego"
        db.session.commit()

        return {'respuesta':'Se actualizo'},200

    #Delete
    def delete(self):
        #busqueda
        tipo_db = db.session.execute(db.select(TipoModelo).where(TipoModelo.codigo_tipo == 1)).scalar_one()
        #eliminacion
        db.session.delete(tipo_db)
        db.session.commit()

        return {'respuesta':'Se elimino'},200