from flask_restx import Api,Namespace
from src.controlador.inicio_sesion_controlador import InicioSesionControlador

def InicioSesionRutas(api):
    ns_inicio = Namespace(name='inicio_sesion',description='Describe el conjunto de endpoinsta para inicio de sesion')
    #estas rutas son para eliminar,consultar, editar y buscar
    ns_inicio.add_resource(InicioSesionControlador,'')


    api.add_namespace(ns_inicio)