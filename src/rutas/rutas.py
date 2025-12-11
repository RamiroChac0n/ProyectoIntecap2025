from flask_restx import Namespace,Api
from src.rutas.tipo_rutas import TipoRutas
from src.rutas.pokemon_rutas import PokemonRutas
from src.rutas.pokemon_x_tipo_rutas import PokemonXTipoRutas

#como una funcion que recibe la 'api'
def RutasGeneral(api:Api):

    #manejo de rutas para tipos
    TipoRutas(api)

    #manejo de rutas para pokemon
    PokemonRutas(api)

    PokemonXTipoRutas(api)

