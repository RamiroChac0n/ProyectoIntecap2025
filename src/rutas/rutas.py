from flask_restx import Namespace,Api
from src.rutas.tipo_rutas import TipoRutas

#como una funcion que recibe la 'api'
def RutasGeneral(api:Api):

    #manejo de rutas para tipos
    TipoRutas(api)

