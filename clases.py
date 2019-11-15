# author <<Kevin Samuel Rodrigues Toledo>>
'''
Sistema de Pedidos de Farmacias

'''

import abc
from abc import *
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

    def __str__(self):
        return self.codigo + " " + self.descripcion


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
        ''' Implementacion del metodo de la operacion de obtencion de articulos organizados en categoria '''
        articulo_categorizado = {
            constants.key_medicamento: [], constants.key_higiene: [], constants.key_belleza: []}
        for articulo in self.articulos:
            if isinstance(articulo, Medicamento):
                articulo_categorizado[constants.key_medicamento].append(
                    articulo)
            elif isinstance(articulo, Higiene):
                articulo_categorizado[constants.key_higiene].append(
                    articulo)
            elif isinstance(articulo, Belleza):
                articulo_categorizado[constants.key_belleza].append(
                    articulo)

        return articulo_categorizado

    def realizar_pedido(self, articulos):
        orden = Orden(articulos)
        self.ordenes.append(orden)
        return orden   

    def cobrar_pedido(self, orden, medio_pago, cliente):
        comprobante = Comprobante(orden, medio_pago, cliente)
        return comprobante

    def obtener_reporte(self):
        pass

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
    numero_documento = 0
    descripcion = 'Pedido' # TODO debe ser una constante
    def __init__(self, articulos, *args):
        super().__init__(self.numero_documento, self.descripcion)
        self._articulos = articulos
        self.numero_orden = None

    def set_numero_orden(self, identificador):
        if identificador > 0:
            self.numero_orden = identificador

    # TODO agregar solamente si es de tipo articulo
    def agregar_articulo(self, articulo):
        ''' Metodo para continuar agregando un articulo a la orden ya creada 
        '''
        self.articulos.append(articulo)

    # TODO corregir
    def __str__(self):
        return 'Numero de orden: ' + str(Orden.numero_orden)

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

# TODO debe ser abstracto (revisar todo)
class Comprobante:
    @abstractmethod
    def __init__(self, orden, medio_pago, cliente):
        self.orden = orden
        self.medio_pago = medio_pago
        self.cliente = cliente


class Factura(Comprobante):
    def __init__(self, *args):
        super.__init__(args)
