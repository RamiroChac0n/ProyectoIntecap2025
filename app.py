
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, TEXT, Date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


app = Flask(__name__)
api = Api(app)




db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin1234@127.0.0.1:5050/pokemon_db"

db.init_app(app)


#crear modelos
class TipoModelo(db.Model):
    __tablename__='tipo'
    codigo_tipo:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nombre:Mapped[str] = mapped_column(String(100),nullable=False)






#http://127.0.0.1:5000/
@api.route('/tipo')
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
    
if __name__ == '__main__':
    app.run(debug=True)