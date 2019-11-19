# author <<Kevin Samuel Rodrigues Toledo>>
'''
Sistema de Pedidos de Farmacias

'''

import abc
from abc import *
import utiles
import datetime

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
    def vender(self, cantidad):
        pass


class Articulo(Vendible):
    def __init__(self, codigo, descripcion, precio_unitario, stock):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.stock = stock

    def vender(self, cantidad):
        self.stock -= cantidad

    def __str__(self):
        return self.codigo + " " + self.descripcion


class Medicamento(Articulo):
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
            utiles.key_medicamento: [], utiles.key_higiene: [], utiles.key_belleza: []}
        for articulo in self.articulos:
            if isinstance(articulo, Medicamento):
                articulo_categorizado[utiles.key_medicamento].append(
                    articulo)
            elif isinstance(articulo, Higiene):
                articulo_categorizado[utiles.key_higiene].append(
                    articulo)
            elif isinstance(articulo, Belleza):
                articulo_categorizado[utiles.key_belleza].append(
                    articulo)

        return articulo_categorizado

    def realizar_pedido(self, numero_orden, articulos):
        orden = Orden(numero_orden, articulos)
        self.ordenes.append(orden)
        return orden

    def cobrar_pedido(self, orden, medio_pago, cliente):
        comprobante = Factura((orden, medio_pago, cliente))
        return comprobante

    def obtener_reporte(self, condicion):
        articulos_vendidos = 0
        ganancia_total = 0
        comprobantes = self.comprobantes
        comprobantes_filtrados = filter(condicion, comprobantes)
        # ganancia_total =
        for comprobante in comprobantes_filtrados:
            articulos = comprobante.orden.articulos
            articulos_vendidos += len(articulos)
            ganancia_total += sum(articulo.precio_unitario for articulo in articulos)

        mensaje = ('Ganancia total: {}, Articulos vendidos: {}'
                   .format(ganancia_total, articulos_vendidos))
        return mensaje


class Contacto(metaclass=ABCMeta):
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
        self.nombre = nombre
        self.contacto = contacto
        self.cedula = cedula
        self.apellido = apellido
        self.direccion = direccion
        self.ruc = ruc

    def __str__(self):
        return ('Nombre: {}, Apellido {}, Cedula: {}'
                .format(self.nombre, self.apellido, self.cedula))


class Empleado:
    def __init__(self, persona):
        this.persona = persona


class Cliente:
    def __init__(self, persona):
        self.persona = persona
        self.facturas = []

    def __str__(self):
        return str(self.persona)


class Documento(metaclass=ABCMeta):
    def __init__(self, numero_documento, descripcion):
        self.numero_documento = numero_documento
        self.descripcion = descripcion


class Orden(Documento):
    numero_documento = 0
    descripcion = utiles.documento_orden

    def __init__(self, numero_orden, articulos, *args):
        super().__init__(self.numero_documento, self.descripcion)
        self.articulos = articulos
        self.numero_orden = None
        self.estado = utiles.estado_pendiente

    def agregar_articulo(self, articulo):
        ''' 
            Metodo para continuar agregando un articulo a la orden ya creada 
        '''
        self.articulos.append(articulo)

    def __str__(self):
        mensaje = '\tNumero de orden: ' + str(Orden.numero_orden) + '\n'
        mensaje += '\tArticulos: \n'
        for articulo in self.articulos:
            mensaje += '\t\t' + str(articulo) + '\n'
        return mensaje


class MedioPago(metaclass=ABCMeta):
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
class Comprobante(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, orden, medio_pago, cliente):
        self.orden = orden
        self.medio_pago = medio_pago
        self.cliente = cliente
        self.fecha = datetime.datetime.now()

    def __str__(self):
        return 'fecha: ' + str(self.fecha)

class Factura(Comprobante):
    def __init__(self, *args):
        super.__init__(args)
