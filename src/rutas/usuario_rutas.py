from flask_restx import Api,Namespace
from src.controlador.usuario_controlador import UsuarioControlador,UsuarioPorCodigoControlador

def UsuarioRutas(api:Api):
    ns_usuario = Namespace(name='usuario',description='Describe el conjunto de endpoints para usuario')
    #estas rutas son para crear y actualizar
    ns_usuario.add_resource(UsuarioControlador,'')

    #esta ruta eliminar y busca un tipo por su codigo usuario
    ns_usuario.add_resource(UsuarioPorCodigoControlador,'/codigo_usuario/<int:codigo_usuario>')

    api.add_namespace(ns_usuario)