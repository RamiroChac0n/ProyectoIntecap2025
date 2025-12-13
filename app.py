
from flask import Flask
from src.comun.utilidades import db, api, ma, jwt
from src.rutas.rutas import RutasGeneral

app = Flask(__name__)






app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin1234@127.0.0.1:5050/pokemon_db"
app.config["JWT_SECRET_KEY"] = "admin-super-secret"

#iniciar las rutas
RutasGeneral(api)


db.init_app(app)
api.init_app(app)
ma.init_app(app)
jwt.init_app(app)


    
if __name__ == '__main__':
    app.run(debug=True)