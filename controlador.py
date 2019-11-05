'''
    Sistema de Pedidos en Farmacias

'''

from modelo import *
from clases import *
from vista import *
from os import listdir


class Controlador:
    @staticmethod
    def inicializar():
        '''---------------------- INICIO DE LA APLICACION ---------------------------'''
        Vista.limpiar_pantalla()
        dir_ordenes = 'datos_ordenes/ordenes'
        dir_clientes = 'datos_clientes/clientes'
        dir_empleados = 'datos_empleados/empleados'
        dir_comprobantes = 'datos_comprobantes/comprobantes'
        dir_articulos = 'datos_articulos/articulos'

        modelo_app = Modelo()
        # TODO plantear el uso de diccionarios y clasificar los articulos por:
        #  Medicamentos, Belleza, Higiene, etc
        # Se cargan los articulos existentes
        if Controlador.validar_existe_pickle(dir_articulos):
            print('entra')
            list_articulos = modelo_app.buscar(dir_articulos)
        else:
            list_articulos = []
            modelo_app.crear(dir_articulos, list_articulos)
        farmacia = Farmacia(list_articulos, constants.business_name, constants.business_ruc)

        # se cargan los clientes existentes
        if Controlador.validar_existe_pickle(dir_clientes):
            list_clientes = modelo_app.buscar(dir_clientes)
        else:
            list_clientes = []
            modelo_app.crear(dir_clientes, list_clientes)

        # se cargan los empleados existentes
        if Controlador.validar_existe_pickle(dir_empleados):
            list_empleados = modelo_app.buscar(dir_empleados)
        else:
            list_empleados = []
            modelo_app.crear(dir_empleados, list_empleados)

        # se cargan las ordenes existentes
        if Controlador.validar_existe_pickle(dir_ordenes):
            list_ordenes = modelo_app.buscar(dir_ordenes)
        else:
            list_ordenes = []
            modelo_app.crear(dir_ordenes, list_ordenes)

        # se cargan los comprobantes existentes
        if Controlador.validar_existe_pickle(dir_comprobantes):
            list_comprobantes = modelo_app.buscar(dir_comprobantes)
        else:
            list_comprobantes = []
            modelo_app.crear(dir_comprobantes, list_comprobantes)

        farmacia.comprobantes = list_comprobantes
        farmacia.ordenes = list_ordenes
        farmacia.clientes = list_clientes
        farmacia.articulos = list_articulos
        datos = [list_ordenes, list_clientes, list_empleados,
                 list_comprobantes, list_articulos, farmacia]

        return datos

    @staticmethod
    def validar_existe_pickle(archivopickle, extension='.pickle'):
        '''--------------------- verificar pickle ---------------------'''
        # Metodo estatico que verifica la existencia del archivo pickle
        if os.path.exists(archivopickle + extension):
            return True
        else:
            return False

    @staticmethod
    def guardar_nuevos_datos(list_orden, list_cliente, list_comprobante, list_articulo):
        '''Guarda los datos nuevos en los archivos'''
        dir_ordenes = 'datos_ordenes/ordenes'
        dir_clientes = 'datos_clientes/clientes'
        dir_comprobantes = 'datos_comprobantes/comprobantes'
        dir_articulos = 'datos_articulos/articulos'

        modeloapp = Modelo()
        modeloapp.crear(dir_ordenes, list_orden)
        modeloapp.crear(dir_clientes, list_cliente)
        modeloapp.crear(dir_comprobantes, list_comprobante)
        modeloapp.crear(dir_articulos, list_articulo)
