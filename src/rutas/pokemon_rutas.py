from flask_restx import Api,Namespace
from src.controlador.pokemon_controlador import PokemonControlador, PokemonControladorPorCodigoPokemon

def PokemonRutas(api):
    ns_pokemon = Namespace(name='pokemon',description='Describe el conjunto de endpoints para pokemon')
    #estas rutas son para eliminar,consultar, editar y buscar
    ns_pokemon.add_resource(PokemonControlador,'')

    #esta ruta eliminar y busca un tipo por su codigo tipo
    ns_pokemon.add_resource(PokemonControladorPorCodigoPokemon,'/codigo_pokemon/<int:codigo_pokemon>')

    api.add_namespace(ns_pokemon)