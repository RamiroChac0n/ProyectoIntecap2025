from flask_restx import Api,Namespace
from src.controlador.tipo_controlador import TipoControlador,TipoControladorPorCodigoTipo

def TipoRutas(api:Api):
    ns_tipo = Namespace(name='tipo',description='Describe el conjunto de endpoints para tipo')
    #estas rutas son para eliminar,consultar, editar y buscar
    ns_tipo.add_resource(TipoControlador,'')

    #esta ruta eliminar y busca un tipo por su codigo tipo
    ns_tipo.add_resource(TipoControladorPorCodigoTipo,'/codigo_tipo/<int:codigo_tipo>')

    api.add_namespace(ns_tipo)