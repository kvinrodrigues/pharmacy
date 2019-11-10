'''
    Sistema de Pedidos en Farmacias

'''

from modelo import *
from clases import *
import os


class Controlador:
    farmacia = None
    @staticmethod
    def inicializar():
        '''---------------------- INICIO DE LA APLICACION ---------------------------'''
        dir_ordenes = 'datos_ordenes/ordenes'
        dir_clientes = 'datos_clientes/clientes'
        dir_empleados = 'datos_empleados/empleados'
        dir_comprobantes = 'datos_comprobantes/comprobantes'
        dir_articulos = 'datos_articulos/articulos'

        modelo_app = Modelo()
        # TODO plantear el uso de diccionarios y clasificar los articulos por:
        #  Medicamentos, Belleza, Higiene, etc
        # Se cargan los articulos existentes
        if Controlador.existe_pickle(dir_articulos):
            list_articulos = modelo_app.buscar(dir_articulos)
        else:
            list_articulos = []
            modelo_app.crear(dir_articulos, list_articulos)
        farmacia = Farmacia(
            list_articulos, constants.business_name, constants.business_ruc)
                
        Controlador.farmacia = farmacia

        # se cargan los clientes existentes
        if Controlador.existe_pickle(dir_clientes):
            list_clientes = modelo_app.buscar(dir_clientes)
        else:
            list_clientes = []
            modelo_app.crear(dir_clientes, list_clientes)

        # se cargan los empleados existentes
        if Controlador.existe_pickle(dir_empleados):
            list_empleados = modelo_app.buscar(dir_empleados)
        else:
            list_empleados = []
            modelo_app.crear(dir_empleados, list_empleados)

        # se cargan las ordenes existentes
        if Controlador.existe_pickle(dir_ordenes):
            list_ordenes = modelo_app.buscar(dir_ordenes)
        else:
            list_ordenes = []
            modelo_app.crear(dir_ordenes, list_ordenes)

        farmacia.numer    

        # se cargan los comprobantes existentes
        if Controlador.existe_pickle(dir_comprobantes):
            list_comprobantes = modelo_app.buscar(dir_comprobantes)
        else:
            list_comprobantes = []
            modelo_app.crear(dir_comprobantes, list_comprobantes)

        farmacia.comprobantes = list_comprobantes
        farmacia.ordenes = list_ordenes
        farmacia.clientes = list_clientes
        farmacia.articulos = list_articulos
        farmacia.empleados = list_empleados
        return farmacia

    @staticmethod
    def filtrar_articulos():
        return Controlador.farmacia.obtener_articulos()

    @staticmethod
    def filtrar_articulo_desde(lista, codigo):
        for articulo in lista:
            if articulo.codigo == codigo[0]:
                return articulo
        # TODO debe ser una excepcion?
        return None

    @staticmethod
    def crear_orden(articulos):
        return Controlador.farmacia.realizar_pedido(articulos)
    

    @staticmethod
    def existe_pickle(archivopickle, extension='.pickle'):
        '''--------------------- verificar pickle ---------------------'''
        # Metodo estatico que verifica la existencia del archivo pickle
        if os.path.exists(archivopickle + extension):
            return True
        else:
            return False

    @staticmethod
    def guardar_nuevos_datos(farmacia):
        '''Guarda los datos nuevos en los archivos'''
        dir_ordenes = 'datos_ordenes/ordenes'
        dir_clientes = 'datos_clientes/clientes'
        dir_comprobantes = 'datos_comprobantes/comprobantes'
        dir_articulos = 'datos_articulos/articulos'

        modeloapp = Modelo()
        modeloapp.crear(dir_ordenes, farmacia.ordenes)
        modeloapp.crear(dir_clientes, farmacia.clientes)
        modeloapp.crear(dir_comprobantes, farmacia.comprobantes)
        modeloapp.crear(dir_articulos, farmacia.articulos)
