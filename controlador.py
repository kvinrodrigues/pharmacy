__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

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
        ''' Metodo invocado al iniciar la aplicacion para instanciar 
            e inicializar las referencias necesarias 
        '''
        dir_ordenes = 'datos_ordenes/ordenes'
        dir_clientes = 'datos_clientes/clientes'
        dir_comprobantes = 'datos_comprobantes/comprobantes'
        dir_articulos = 'datos_articulos/articulos'

        modelo_app = Modelo()
        # Se cargan los articulos existentes
        if Controlador.existe_pickle(dir_articulos):
            list_articulos = modelo_app.buscar(dir_articulos)
        else:
            list_articulos = []
            modelo_app.crear(dir_articulos, list_articulos)
        farmacia = Farmacia(
            list_articulos, utiles.NOMBRE_EMPRESA, utiles.RUC_EMPRESA)

        Controlador.farmacia = farmacia

        # se cargan los clientes existentes
        if Controlador.existe_pickle(dir_clientes):
            list_clientes = modelo_app.buscar(dir_clientes)
        else:
            list_clientes = []
            modelo_app.crear(dir_clientes, list_clientes)

        # se cargan las ordenes existentes
        if Controlador.existe_pickle(dir_ordenes):
            list_ordenes = modelo_app.buscar(dir_ordenes)
        else:
            list_ordenes = []
            modelo_app.crear(dir_ordenes, list_ordenes)
        Orden.numero_orden = len(list_ordenes) + 1
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
        return farmacia

    @staticmethod
    def crear_orden(articulos):
        ''' Metodo para realizar la creacion del pedido 
            mediante una orden dentro del sistema 
        '''
        numero_orden = len(Controlador.farmacia.ordenes)
        orden = Controlador.farmacia.realizar_pedido(numero_orden, articulos)
        return orden

    @staticmethod
    def filtrar_articulos():
        ''' Metodo que retorna los articulos que dispone la farmacia '''
        return Controlador.farmacia.obtener_articulos()

    @staticmethod
    def obtener_cliente_por_defecto():
        ''' Metodo para obtener cliente por defecto a utilizar al cobrar pedido '''
        persona = Persona(Email(utiles.CLIENTE_DEFECTO_CONTACTO_VALOR), utiles.CLIENTE_DEFECTO_CI, utiles.CLIENTE_DEFECTO_NOMBRE,
                          utiles.CLIENTE_DEFECTO_APELLIDO, utiles.CLIENTE_DEFECTO_DIRECCION,
                          utiles.CLIENTE_DEFECTO_RUC)
        return Cliente(persona)

    @staticmethod
    def filtrar_articulo_desde(lista, codigo):
        ''' Metodo para obtener un articulo mediante el codigo proveido, 
            apartir de la lista de articulos recibido 
        '''
        for articulo in lista:
            if articulo.codigo == codigo:
                return articulo
        raise Exception('No se encontro el articulo de codigo: ' + codigo)

    @staticmethod
    def registrar_cliente(cedula, nombre, apellido, ruc, direccion, contacto):
        ''' Metodo para proceder a la creacion del cliente en el sistema '''
        cliente = Cliente(
            Persona(contacto, cedula, nombre, apellido, direccion, ruc))
        Controlador.farmacia.clientes.append(cliente)
        return cliente

    @staticmethod
    def obtener_metodo_pago_efectivo():
        ''' Metodo que retorna la instancia del medio de pago tipo efectivo '''
        return Efectivo('Efectivo', 'Pago mediante efectivo')

    @staticmethod
    def obtener_metodo_pago_tarjeta():
        ''' Metodo que retorna la instancia del medio de pago tipo tarjeta '''
        return Tarjeta('Tarjeta', 'Pago mediante tarjeta')

    @staticmethod
    def obtener_categorias_articulos():
        ''' Se retorna una copia de las categorias de articulos disponibles '''
        return [*(utiles.CATEGORIA_ARTICULOS)]

    @staticmethod
    def obtener_articulos_por_categoria(categoria):
        ''' Metodo que retorna los articulos disponibles en la categoria introducida,
            se lanza una excepcion caso que no se encuentre el articulo
        '''
        articulos = []
        try:
            articulos_categorizados = Controlador.filtrar_articulos()
            articulos = articulos_categorizados[categoria]
        except(KeyError):
            raise Exception('No existe la categoria: ' + str(categoria))
        return articulos

    @staticmethod
    def buscar_orden(identificador, estado_busqueda):
        ''' Metodo que retorna orden de acuerdo al numero de orden introducido y el estado esperado '''
        ordenes = Controlador.farmacia.ordenes
        for orden in ordenes:
            estado_orden = orden.estado
            if orden.numero_orden == identificador and estado_orden == estado_busqueda:
                return orden
            elif orden.numero_orden == identificador and not estado_orden == estado_busqueda:
                raise Exception('Estado de orden invalida.')

        raise Exception("No se encontro la orden: " + str(identificador))

    @staticmethod
    def buscar_cliente(numero_cedula):
        ''' Metodo que retorna el cliente mediante el numero de cedula, si no existe retorna None '''
        clientes = Controlador.farmacia.clientes
        for cliente in clientes:
            if cliente.persona.cedula == numero_cedula:
                return cliente
        return None

    @staticmethod
    def obtener_nombre_categoria(identificador):
        return utiles.CATEGORIA_ARTICULOS[identificador]

    @staticmethod
    def crear_comprobante(orden, medio_pago, cliente):
        ''' Metodo para realizar la creacion del comprobante '''
        articulos = orden.articulos
        map(lambda articulo: articulo.vender(1), articulos) # por cada articulo se realiza la reduccion de stock
        comprobante = Controlador.farmacia.cobrar_pedido(
            orden, medio_pago, cliente)
        return comprobante

    @staticmethod
    def farmacia_existen_articulos():
        '''Metodo para verificar si existen articulos en la farmacia'''
        return not len(Controlador.farmacia.articulos) == 0

    @staticmethod
    def guardar_comprobante(comprobante):
        ''' Metodo encargado de guardar comprobante en la farmacia '''
        Controlador.farmacia.comprobantes.append(comprobante)

    @staticmethod
    def filtrar_comprobantes(condicion):
        ''' Metodo para obtener los comprobantes correspondiente a la condicion recibida '''
        return Controlador.farmacia.obtener_reporte(condicion)

    @staticmethod
    def definicion_filtro_comprobante_diario(anio, mes = 1, dia = 1):
        ''' Metodo que retorna la condicion que se debe cumplir para filtrar comprobantes por dia '''
        return (lambda factura: factura.fecha.year == anio
                and factura.fecha.month == mes 
                and factura.fecha.day == dia)

    @staticmethod
    def numero_de_semana_por_mes(date_value):
        ''' Metodo para obtener el numero de semana del mes de la fecha recibida como parametro'''
        # Se obtiene la diferencia entre la semana del anio en base a la fecha y la semana del dia que comienza el mes
        # luego se adiciona 1
        return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)

    @staticmethod
    def es_mes_valido(mes):
        return mes > 0 and mes <= 12

    @staticmethod
    def es_dia_valido(dia):
        return dia > 0 and dia <= 31

    @staticmethod
    def definicion_filtro_comprobante_semanal(semana, mes, anio):
        ''' Metodo que retorna la condicion que se debe cumplir para filtrar comprobantes por semana '''
        return (lambda factura: Controlador.numero_de_semana_por_mes(factura.fecha) == semana
                and factura.fecha.month == mes and factura.fecha.year == anio)

    @staticmethod
    def definicion_filtro_comprobante_mensual(anio, mes):
        ''' Metodo que retorna la condicion que se debe cumplir para filtrar comprobantes por mes '''
        return (lambda factura: factura.fecha.month == mes and factura.fecha.year == anio)

    @staticmethod
    def definicion_filtro_comprobante_anual(anio):
        ''' Metodo que retorna la condicion que se debe cumplor para filtrar comprobantes por anio '''
        return (lambda factura: factura.fecha.year == anio)

    @staticmethod
    def existe_pickle(archivopickle, extension='.pickle'):
        ''' Metodo que verifica la existencia del archivo pickle '''
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
