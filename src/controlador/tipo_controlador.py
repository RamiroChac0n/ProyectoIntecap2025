
from flask_restx import Resource
from src.comun.utilidades import db
from src.modelo.tipo_modelo import TipoModelo
from sqlalchemy.orm.exc import NoResultFound


#busqueda de todos
#busqueda por parametros
#eliminacion de todos
#eliminacion por id
#creacion
#actualizacion

#parametros
#eliminacion y busqueda por tipo por su codigo tipo
class TipoControladorPorCodigoTipo(Resource):

    #select * from table condicion
    def get(self, codigo_tipo:int):
        try:
            #buscar el elemento a ver si existe
            tipo_db = db.session.execute(db.select(TipoModelo).where(TipoModelo.codigo_tipo == codigo_tipo)).scalar_one()

            return {
                'codigo_tipo':tipo_db.codigo_tipo,
                'nombre': tipo_db.nombre
            },200

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
    def post(self):
        #crear tipo
        tipo =  TipoModelo(nombre="Fuego")
        db.session.add(tipo)
        db.session.commit()
        return {'respuesta':'Se creo'},201
    
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