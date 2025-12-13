
from flask import Flask
from src.comun.utilidades import db, api, ma, jwt
from src.rutas.rutas import RutasGeneral

app = Flask(__name__)




app.config.from_object("configuracion.Configuracion")

#iniciar las rutas
RutasGeneral(api)


db.init_app(app)
api.init_app(app)
ma.init_app(app)
jwt.init_app(app)


    
if __name__ == '__main__':
    app.run(debug=True)