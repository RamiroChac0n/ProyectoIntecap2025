from flask_restx import Api,Namespace
from src.controlador.pokemon_x_tipo_controlador import PokemonXTipoControlador,PokemonXTipoPorCodigosControlador

def PokemonXTipoRutas(api):
    ns_pokemon = Namespace(name='pokemon_x_tipo',description='Describe el conjunto de endpoints para pokemon por tipo')
    #estas rutas son para eliminar,consultar, editar y buscar
    ns_pokemon.add_resource(PokemonXTipoControlador,'')

    #esta ruta eliminar y busca un tipo por su codigo tipo
    ns_pokemon.add_resource(PokemonXTipoPorCodigosControlador,'/codigo_pokemon/<int:codigo_pokemon>/codigo_tipo/<int:codigo_tipo>')

    api.add_namespace(ns_pokemon)