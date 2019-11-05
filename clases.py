# author <<Kevin Samuel Rodrigues Toledo>>
'''
Sistema de Pedidos de Farmacias

'''

import abc
from abc import *
from vista import *
import constants
# Abstract


class Empresa(metaclass=ABCMeta):
    '''Clase abstracta de Empresa'''
    @abstractmethod
    def __init__(self, nombre, ruc):
        ''' Inicializador de objetos de la clase Empresa'''
        self.__nombre = nombre
        self.__ruc = ruc


class Vendible:
    @abstractmethod
    def vender(self):
        pass


class Articulo(Vendible):
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion


class Medicamento(Articulo):
    # TODO implementar
    def vender(self):
        return super().vender()    

class Belleza(Articulo):
    def vender(self):
        return super().vender()


class Higiene(Articulo):
    def vender(self):
        return super().vender()


class Farmacia(Empresa):
    '''Clase de la farmacia'''

    def __init__(self, articulos, *args):
        super().__init__(*args)
        self.articulos = articulos
        self.empleados = []
        self.clientes = []
        self.ordenes = []
        self.comprobantes = []

    def obtener_articulos(self):
        ''' Implementacion del metodo de la operacion del listado de articulos '''
        articulo_categorizado = {
            constants.tipo_medicamento: [], constants.tipo_higiente: [], constants.tipo_belleza: []}
        for articulo in self.articulos:
            if isinstance(articulo, Medicamento):
                articulo_categorizado[constants.tipo_medicamento].append(
                    articulo)
            elif isinstance(articulo, Higiene):
                articulo_categorizado[constants.tipo_higiente].append(articulo)
            elif isinstance(articulo, Belleza):
                articulo_categorizado[constants.tipo_belleza].append(articulo)

        return articulo_categorizado

    def listar_articulos(self):
        '''Metodo para listar los articulos existentes'''
        articulos_categorizados = self.obtener_articulos()
        Vista.listar_articulos(articulos_categorizados)

    def realizar_pedido(self):
        pass

    def obtener_comprobante(self, numero_orden):
        pass

    def obtener_reporte(self):
        pass

# TODO implementar correctamente esta abstraccion


class Contacto():
    @abstractmethod
    def __init__(self):
        pass


class Telefono(Contacto):
    pass


class Email(Contacto):
    pass


class RedSocial(Contacto):
    pass


class Persona:
    @abstractmethod
    def __init__(self, contacto, cedula, nombre, apellido, direccion, ruc):
        self.contacto = contacto
        self.cedula = cedula
        self.apellido = apellido
        self.direccion = direccion
        self.ruc = ruc


class Empleado:
    def __init__(self, persona):
        this.persona = persona


class Cliente:
    def __init__(self, persona):
        self.persona = persona
        self.facturas = []


class Documento:
    def __init__(self, numero_documento, descripcion):
        self.numero_documento = numero_documento
        self.descripcion = descripcion


class Orden(Documento):
    def __init__(self, numero_orden, articulos, *args):
        super().__init__(args)
        self.numero_orden = numero_orden
        self.articulos = articulos

    # TODO agregar solamente si es de tipo articulo
    def agregar_articulo(self, articulo):
        self.articulos.append(articulo)


class MedioPago:
    @abstractmethod
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Efectivo(MedioPago):
    def __init__(self, *args):
        super().__init__(args)


class Tarjeta(MedioPago):
    def __init__(self, *args):
        super().__init__(args)


class Comprobante:
    @abstractmethod
    def __init__(self, orden, medio_pago, cliente):
        self.orden = orden
        self.medio_pago = medio_pago
        self.cliente = cliente


class Factura(Comprobante):
    def __init__(self, *args):
        super.__init__(args)
