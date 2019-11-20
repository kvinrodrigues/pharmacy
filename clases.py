__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

'''
Sistema de Pedidos de Farmacias

'''

import abc
from abc import *
import utiles
import datetime


class Empresa(metaclass=ABCMeta):
    '''Clase abstracta de la empresa'''
    @abstractmethod
    def __init__(self, nombre, ruc):
        ''' Inicializador abstracto de objetos de la clase Empresa'''
        self.__nombre = nombre
        self.__ruc = ruc


class Vendible:
    ''' Clase abstracta que define la operacion de vender '''
    @abstractmethod
    def vender(self, cantidad):
        pass


class Articulo(Vendible, metaclass=ABCMeta):
    ''' Clase abstracta del articulo '''

    def __init__(self, codigo, descripcion, precio_unitario, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.stock = stock

    def vender(self, cantidad):
        ''' Metodo que implementa la operacion de venta '''
        self.stock -= cantidad

    def __str__(self):
        return ('Codigo: {}, descripcion: {}, precio: {}'
                .format(self.codigo, self.descripcion, self.precio_unitario))


class Medicamento(Articulo):
    ''' Clase medicamento, el cual es un articulo '''

    def vender(self, cantidad):
        super().vender()

    def __str__(self):
        return self.codigo + " " + self.descripcion


class Belleza(Articulo):
    ''' Clase belleza, el cual es un articulo '''

    def vender(self, cantidad):
        super().vender()

    def __str__(self):
        return self.codigo + " " + self.descripcion


class Higiene(Articulo):
    ''' Clase higiene, el cual es un articulo '''

    def vender(self, cantidad):
        super().vender()

    def __str__(self):
        return self.codigo + " " + self.descripcion


class Farmacia(Empresa):
    '''Clase de la farmacia'''

    def __init__(self, articulos, *args):
        super().__init__(*args)
        self.articulos = articulos
        self.clientes = []
        self.ordenes = []
        self.comprobantes = []

    def obtener_articulos(self):
        ''' Implementacion del metodo de la operacion de obtencion de articulos organizados en categoria '''
        articulo_categorizado = {
            utiles.KEY_MEDICAMENTO: [], utiles.KEY_HIGIENE: [], utiles.KEY_BELLEZA: []}
        for articulo in self.articulos:
            if isinstance(articulo, Medicamento):
                articulo_categorizado[utiles.KEY_MEDICAMENTO].append(
                    articulo)
            elif isinstance(articulo, Higiene):
                articulo_categorizado[utiles.KEY_HIGIENE].append(
                    articulo)
            elif isinstance(articulo, Belleza):
                articulo_categorizado[utiles.KEY_BELLEZA].append(
                    articulo)

        return articulo_categorizado

    def realizar_pedido(self, numero_orden, articulos):
        ''' Metodo para realizar pedido mediante las ordenes '''
        orden = Orden(numero_orden, articulos)
        self.ordenes.append(orden)
        return orden

    def cobrar_pedido(self, orden, medio_pago, cliente):
        ''' Metodo para proceder a la venta, cobrando el pedido '''
        comprobante = Factura(orden, medio_pago, cliente)
        return comprobante

    def obtener_reporte(self, condicion):
        ''' Metodo para obtener un mensaje resumido de las 
            ventas realizadas segun condicion establecida 
        '''
        articulos_vendidos = 0
        ganancia_total = 0
        comprobantes = self.comprobantes
        comprobantes_filtrados = filter(condicion, comprobantes)
        for comprobante in comprobantes_filtrados:
            articulos = comprobante.orden.articulos
            articulos_vendidos += len(articulos)
            ganancia_total += sum(articulo.precio_unitario for articulo in articulos)

        mensaje = ('Ganancia total: {}, Articulos vendidos: {}'
                   .format(ganancia_total, articulos_vendidos))
        return mensaje


class Contacto(metaclass=ABCMeta):
    ''' Clase abstracta del contacto '''
    @abstractmethod
    def __init__(self, valor):
        self.valor = valor


class Telefono(Contacto):
    ''' Clase telefono, el cual es un contacto '''

    def __init__(self, prefijo, *args):
        super().__init__(*args)
        self.prefijo = prefijo


class Email(Contacto):
    ''' Clase email, el cual es un contacto '''

    def __init__(self, *args):
        super().__init__(*args)


class RedSocial(Contacto):
    ''' Clase red social, el cual es un contacto '''

    def __init__(self, *args):
        super().__init__(*args)


class Persona:
    ''' Clase que representa una persona '''

    def __init__(self, contacto, cedula, nombre, apellido, direccion, ruc):
        self.nombre = nombre
        self.contacto = contacto
        self.cedula = cedula
        self.apellido = apellido
        self.direccion = direccion
        self.ruc = ruc

    def __str__(self):
        return ('Nombre: {}, Apellido {}, Cedula: {}'
                .format(self.nombre, self.apellido, self.cedula))


class Cliente:
    ''' Clase cliente que se compone de una Persona '''

    def __init__(self, persona):
        self.persona = persona
        self.facturas = []

    def __str__(self):
        return str(self.persona)


class Documento(metaclass=ABCMeta):
    ''' Clase que representa un documento '''
    @abstractmethod
    def __init__(self, numero_documento, descripcion):
        self.numero_documento = numero_documento
        self.descripcion = descripcion


class Orden(Documento):
    ''' Clase orden el cual es un documento a utilizar en el flujo del sistema '''
    numero_documento = utiles.NUMERO_DOC_ORDEN
    descripcion = utiles.DOCUMENTO_ORDEN

    def __init__(self, numero_orden, articulos, *args):
        super().__init__(self.numero_documento, self.descripcion)
        self.articulos = articulos
        self.numero_orden = numero_orden
        self.estado = utiles.ESTADO_PENDIENTE

    def __str__(self):
        mensaje = '\tNumero de orden: ' + str(self.numero_orden) + '\n'
        mensaje += '\tArticulos: \n'
        for articulo in self.articulos:
            mensaje += '\t\t' + str(articulo) + '\n'
        return mensaje


class MedioPago(metaclass=ABCMeta):
    ''' Clase abstracta que representa al medio de pago  '''
    @abstractmethod
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Efectivo(MedioPago):
    ''' Clase efectivo, el cual es un medio de pago '''

    def __init__(self, *args):
        super().__init__(*args)


class Tarjeta(MedioPago):
    ''' Clase tarjeta, el cual es un medio de pago '''

    def __init__(self, *args):
        super().__init__(*args)


class Comprobante(metaclass=ABCMeta):
    ''' Clase abstracta que representa al comprobante '''
    @abstractmethod
    def __init__(self, orden, medio_pago, cliente):
        self.orden = orden
        self.medio_pago = medio_pago
        self.cliente = cliente
        self.fecha = datetime.datetime.now()

    def __str__(self):
        return 'fecha: ' + str(self.fecha)


class Factura(Comprobante):
    ''' Clase factura, el cual es un comprobante '''

    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        orden = self.orden
        monto_total = 0
        mensaje = 'Factura: \n\t\tNumero de orden: {}'.format(
            orden.numero_orden)
        mensaje += '\n\t\t Articulos: '
        for articulo in orden.articulos:
            mensaje += '\n\t\t\t' + str(articulo)
            monto_total += articulo.precio_unitario
        mensaje += "\n\t\tMonto total: " + str(monto_total)
        return mensaje
