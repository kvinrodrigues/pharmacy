__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

'''
    Sistema de Pedidos en Farmacias

'''

from controlador import *
import os
import sys
import logging
import utiles


class VistaConsola:
    @staticmethod
    def realizar_pedido():
        try:
            articulos = []
            articulos = VistaConsola.seleccionar_articulos(articulos)
            if articulos:
                orden = Controlador.crear_orden(articulos)
                VistaConsola.limpiar_pantalla()
                VistaConsola.imprimir('Detalle de la orden creada: ')
                VistaConsola.imprimir(str(orden))
            else:
                raise Exception('Debe introducir por lo menos un articulo.')
        except Exception as e:
            VistaConsola.imprimir(str(e))
            VistaConsola.imprimir('No se pudo generar la orden...')

        VistaConsola.pausa()

    @staticmethod
    def cobrar_pedido():
        VistaConsola.imprimir('Introduzca numero de orden: ')
        try:
            entrada = VistaConsola.leer_numero()
            orden = Controlador.buscar_orden(
                entrada, utiles.ESTADO_PENDIENTE)
            VistaConsola.imprimir('Introduzca numero de cedula: ')
            entrada_cedula = VistaConsola.leer_numero()
            cliente = Controlador.buscar_cliente(entrada_cedula)
            if cliente is None:
                VistaConsola.imprimir(
                    'Desea crear el cliente de cedula: ' + str(entrada_cedula) + '?')
                VistaConsola.imprimir('Y: Si, N: No')
                desea_registrar = VistaConsola.leer_cadena()
                if desea_registrar[0] == 'Y':
                    cliente = VistaConsola.registrar_cliente(entrada_cedula)
                elif desea_registrar[0] == 'N':
                    cliente = Controlador.obtener_cliente_por_defecto()
                else:
                    raise Exception('Opcion invalida')
            VistaConsola.pausa()
            medio_pago = VistaConsola.seleccionar_metodo_pago()
            comprobante = Controlador.crear_comprobante(
                orden, medio_pago, cliente)
            cliente.facturas.append(comprobante)
            orden.estado = utiles.ESTADO_PAGADO
            Controlador.guardar_comprobante(comprobante)
            VistaConsola.imprimir('Cobro realizado con exito: ')
            VistaConsola.imprimir(str(comprobante))
        except Exception as e:
            VistaConsola.imprimir('No se pudo realizar el cobro: ' + str(e))

        VistaConsola.pausa()

    @staticmethod
    def seleccionar_metodo_pago():
        ''' 
            Metodo que permite ingresar el tipo de medio de pago a utilizar
        '''
        VistaConsola.limpiar_pantalla()
        VistaConsola.imprimir(
            '----------- Seleccion Metodo de Pago ------------')
        VistaConsola.imprimir(
            'Seleccione metodo de pago: 1: Efectivo, 2: Tarjeta')
        metodo_pago = {1: Controlador.obtener_metodo_pago_efectivo(
        ), 2: Controlador.obtener_metodo_pago_tarjeta()}
        entrada = VistaConsola.leer_numero()
        return metodo_pago[entrada]

    @staticmethod
    def desplegar_articulos():
        VistaConsola.limpiar_pantalla()
        VistaConsola.imprimir(
            '---------- Listado de Articulos en categoria ----------')
        # DICCIONARIO que posee los articulos disponibles en categoria
        articulos_categorizados = Controlador.filtrar_articulos()
        articulos_higiene = articulos_categorizados[utiles.KEY_HIGIENE]
        articulos_medicamento = articulos_categorizados[utiles.KEY_MEDICAMENTO]
        articulos_belleza = articulos_categorizados[utiles.KEY_BELLEZA]
        if not Controlador.farmacia_existen_articulos():
            VistaConsola.farmacia_sin_articulos()
        else:
            mensaje = ('\n--- LISTA DE ARTICULOS DISPONIBLES: ---\n')
            mensaje = mensaje + ('\t--- MEDICAMENTOS: --- \n')
            for medicamento in articulos_medicamento:
                mensaje = (mensaje + '\t\t' + medicamento.descripcion + '\n')

            mensaje = mensaje + ('\t--- ARTICULOS DE HIGIENE PERSONAL: --- \n')
            for higiene in articulos_higiene:
                mensaje = (mensaje + '\t\t' + higiene.descripcion + '\n')

            mensaje = mensaje + ('\t--- ARTICULOS DE BELLEZA: --- \n')
            for belleza in articulos_belleza:
                mensaje = (mensaje + '\t\t' + belleza.descripcion + '\n')
            VistaConsola.imprimir(mensaje)
        VistaConsola.pausa()

    @staticmethod
    def gestionar_informe():
        try:
            acciones = {'DD': lambda: VistaConsola.obtener_informe_diario(),
                        'MM': lambda: VistaConsola.obtener_informe_mensual(),
                        'YY': lambda: VistaConsola.obtener_informe_anual(),
                        'WW': lambda: VistaConsola.obtener_informe_semanal()}
            VistaConsola.imprimir('Seleccione periodo de tiempo')
            VistaConsola.imprimir(
                'Diario: DD, Semana: WW, Mensual: MM, Anual: YY')
            entrada = VistaConsola.leer_cadena()
            utiles.realizar(acciones[entrada[0]])
        except Exception as e:
            VistaConsola.imprimir(
                "Error al intentar obtener informe: " + str(e))
        VistaConsola.pausa()

    @staticmethod
    def obtener_informe_diario():
        VistaConsola.imprimir('Introduzca anio: ')
        anio = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca mes: ')
        mes = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca dia')
        dia = VistaConsola.leer_numero()
        condicion = Controlador.definicion_filtro_comprobante_diario(
            anio, mes, dia)
        reporte = Controlador.filtrar_comprobantes(condicion)
        VistaConsola.imprimir(reporte)

    @staticmethod
    def obtener_informe_semanal():
        VistaConsola.imprimir('Introduzca anio: ')
        anio = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca mes: ')
        mes = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca semana')
        semana = VistaConsola.leer_numero()
        condicion = Controlador.definicion_filtro_comprobante_semanal(
            semana, mes, anio)
        reporte = Controlador.filtrar_comprobantes(condicion)
        VistaConsola.imprimir(reporte)

    @staticmethod
    def obtener_informe_mensual():
        VistaConsola.imprimir('Introduzca anio: ')
        anio = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca mes: ')
        mes = VistaConsola.leer_numero()
        condicion = Controlador.definicion_filtro_comprobante_mensual(
            anio, mes)
        reporte = Controlador.filtrar_comprobantes(condicion)
        VistaConsola.imprimir(reporte)

    @staticmethod
    def obtener_informe_anual():
        VistaConsola.imprimir('Introduzca anio: ')
        entrada = VistaConsola.leer_numero()
        condicion = Controlador.definicion_filtro_comprobante_anual(entrada)
        reporte = Controlador.filtrar_comprobantes(condicion)
        VistaConsola.imprimir(reporte)

    @staticmethod
    def registrar_cliente(numero_cedula):
        ''' 
            Metodo para registrar un cliente en el sistema
        '''
        VistaConsola.imprimir('Introduzca nombre: ')
        nombre = VistaConsola.leer_cadena()[0]
        VistaConsola.imprimir('Introduzca apellido')
        apellido = VistaConsola.leer_cadena()[0]
        VistaConsola.imprimir('Introduzca direccion: ')
        direccion = VistaConsola.leer_cadena()[0]
        VistaConsola.imprimir('Introduzca RUC')
        ruc = VistaConsola.leer_cadena()[0]
        contactos = VistaConsola.seleccionar_contactos()
        cliente = Controlador.registrar_cliente(numero_cedula,
                                                nombre, apellido, ruc, direccion, contactos)
        VistaConsola.imprimir(
            'Cliente registrado exitosamente: ' + str(cliente))
        return cliente

    @staticmethod
    def seleccionar_contactos():
        VistaConsola.imprimir('--------- Seleccion de contactos ----------')
        contactos = []
        while(True):
            opcion = {1: lambda: VistaConsola.seleccionar_contacto_telefono(),
                      2: lambda: VistaConsola.seleccionar_contacto_email(),
                      3: lambda: VistaConsola.seleccionar_contacto_red_social()}
            VistaConsola.imprimir('Seleccione tipo de contacto: {}, {}, {}, {}'
                                  .format('1. Telefono', '2: Email', '3: Red Social', '-1: Finalizar'))
            entrada = VistaConsola.leer_numero()
            if (entrada == -1):
                return contactos
            contactos.append(utiles.realizar(opcion[entrada]))

    @staticmethod
    def seleccionar_contacto_telefono():
        ''' Metodo para selecciona un contacto de tipo telefonico '''
        VistaConsola.imprimir('Introduzca prefijo: ')
        prefijo = VistaConsola.leer_numero()
        VistaConsola.imprimir('Introduzca valor: ')
        valor = VistaConsola.leer_numero()
        return Telefono(prefijo, valor)

    @staticmethod
    def seleccionar_contacto_email():
        ''' Metodo para selecciona un contacto de tipo correo electronico '''
        VistaConsola.imprimir('Introduzca valor')
        valor = VistaConsola.leer_cadena()
        return Email(valor)

    @staticmethod
    def seleccionar_contacto_red_social():
        ''' Metodo para selecciona un contacto de tipo red social '''
        VistaConsola.imprimir('Introduzca valor: ')
        valor = VistaConsola.leer_cadena()
        return RedSocial(valor)

    # Metodo para limpiar la pantalla
    @staticmethod
    def limpiar_pantalla():
        '''Limpia la pantalla de la sesion utilizada'''
        os.system('cls' if os.name == 'nt' else 'clear')

    # Metodo para la lectura de numeros con manejo de excepciones
    @staticmethod
    def leer_numero(mensaje='', valor_minimo=-1, valor_maximo=None, default=None):
        ''' Se valida para establecer un rango de validez
         :param str mensaje: El mensaje a mostrar al usuario
         :param int valor_minimo: Valor minimo aceptable
         :param int valor_maximo: Valor maximo aceptable
         :param int default: Valor por defecto
        '''
        activo = True
        valor = input(mensaje)
        valor = valor or default
        try:
            valor_numerico = int(valor)
            if ((valor_maximo != None) and (valor_numerico < valor_minimo or
                                            valor_numerico > valor_maximo)) or ((valor_maximo == None)
                                                                                and (valor_numerico < valor_minimo)):
                raise Exception("Introduzca argumentos validos")
            else:
                activo = False
                return valor_numerico
        except ValueError as e:
            raise ValueError("Debe ingresar un número")
        except TypeError as e:
            raise Exception("Debe ingresar un número")
        except Exception as e:
            raise (e)

    @staticmethod
    def leer_cadena(mensaje='', default=None):
        ''' Funcion que obtiene una cadena
         :param str mensaje: El mensaje a mostrar al usuario
         :param str default: Valor por defecto
         '''
        if default:
            mensaje = mensaje + default + chr(8) * len(default)
        entrada = input(mensaje)
        entrada = entrada or default
        try:
            if entrada == None:
                raise Exception("Debe ingresar el dato!")
            # Se retorna una lista con el valor válido ingresado por el usuario
            # Y el boolean True indicando que se pudo concretar la lectura
            return [entrada, True]

            # En caso de algun error, se retorna una lista con el error
            # Y un boolean False que indica el error
        except ValueError as e:
            return ["Vuelva a ingresar el dato", False]
        except TypeError as e:
            return ["Vuelva a ingresar el dato", False]
        except Exception as e:
            return [e, False]

    @staticmethod
    def pausa():
        '''Confirmación para continuar'''
        entrada = input("Continuar... ")
        return

    @staticmethod
    def error_menu():
        '''Error en la seleccion del menú'''
        mensaje = "Error: Opción seleccionada no existe. Vuelva a intentarlo"
        VistaConsola.imprimir(mensaje)

    @staticmethod
    def menu_principal():
        ''' Vista del menú principal'''
        VistaConsola.limpiar_pantalla()
        mensaje = ("---------------- Bienvenido al Sistema de Pedidos para Farmacias ---------------\n" +
                   "------------------- Menú Principal ----------------- \n" +
                   "Ingrese el número correspondiente a la opción deseada: \n"
                   + "1. Realizar pedido \n"
                   + "2. Cobrar pedido \n"
                   + "3. Listar Articulos \n"
                   + "4. Obtener informe \n"
                   + "0. Salir")
        VistaConsola.imprimir(mensaje)

        while(True):
            VistaConsola.imprimir("Accion: ")
            opcion_menu = VistaConsola.leer_numero()
            if isinstance(opcion_menu, str):
                VistaConsola.imprimir(opcion_menu)
            else:
                break

        return opcion_menu

    @staticmethod
    def cerrar_aplicacion():
        '''Confirmación para cerrar la aplicación'''
        mensaje = ("--------------- Cerrar aplicación ----------------\n" +
                   "\n Está Seguro? \t\tSí = 1 \t\tNo = 0 ")
        VistaConsola.imprimir(mensaje)
        entrada = VistaConsola.leer_numero('Confirme: ', 0, 1, 0)
        if (entrada == 1):
            sys.exit()

    @staticmethod
    def farmacia_sin_articulos():
        '''Mensaje de Farmacia sin articulos'''
        mensaje = ("---------------- FARMACIA FUERA DE STOCK ---------------\n" +
                   "Por favor, regrese mas tarde.")
        VistaConsola.imprimir(mensaje)

    @staticmethod
    def seleccionar_categoria():
        return VistaConsola.leer_numero("Ingrese categoria: ")

    @staticmethod
    def imprimir_opciones_categorias():
        mensaje = (
            '------------------- Categorias Disponibles ----------------------------')
        categorias = Controlador.obtener_categorias_articulos()
        for id in categorias:
            mensaje += '\n'
            mensaje += str(id) + '- ' + \
                Controlador.obtener_nombre_categoria(id)
        mensaje += '\n'
        mensaje += '-----------------------------------------------------------------------'
        VistaConsola.imprimir(mensaje)

    @staticmethod
    def seleccionar_articulos(articulos_seleccionados):
        '''
            Metodo para seleccionar articulos
        '''
        VistaConsola.limpiar_pantalla()
        mensaje = ("--------- Seleccione categoria del articulo ---------")
        VistaConsola.imprimir(mensaje)
        VistaConsola.imprimir_opciones_categorias()
        categoria_seleccionada = VistaConsola.seleccionar_categoria()
        try:
            articulos_en_categoria = Controlador.obtener_articulos_por_categoria(
                categoria_seleccionada)
            VistaConsola.limpiar_pantalla()
            VistaConsola.imprimir('Articulos de la categoria: ' +
                                  str(categoria_seleccionada))
            for articulo in articulos_en_categoria:
                VistaConsola.imprimir(articulo)
            VistaConsola.imprimir(
                'Ingrese identificadores de los articulos, enter para confirmar.')
            VistaConsola.imprimir(
                'Ingrese numero de articulo: -1 para confirmar; -2 volver atras')
            articulos_parciales = VistaConsola.seleccionar_articulos_desde(
                articulos_en_categoria)
            articulos_seleccionados.extend(articulos_parciales)
            return articulos_seleccionados

        except Exception as e:
            VistaConsola.imprimir(e)
            raise e

    @staticmethod
    def seleccionar_articulos_desde(articulo_en_categoria):
        '''
            Metodo para seleccionar articulos en base al listado de categorias
        '''
        articulos = []
        entrada = VistaConsola.leer_cadena()
        while(not entrada[0] == '-1'):
            if entrada[0] == '-2':
                VistaConsola.seleccionar_articulos(articulos)
                break
            if entrada[0] == '-3':
                return []
            articulo = Controlador.filtrar_articulo_desde(
                articulo_en_categoria, entrada[0])
            if articulo is not None:
                articulos.append(articulo)
            else:
                VistaConsola.imprimir(
                    'No se pudo agregar el articulo ingresado.')
            entrada = VistaConsola.leer_cadena()
        return articulos

    @staticmethod
    def imprimir(mensaje):
        ''' Mediante este metodo se imprime en la consola '''
        print(mensaje)

    @staticmethod
    def salir():
        '''Confirmación para salir'''
        op = input("Presione enter para salir. ")
        return

    @staticmethod
    def final():
        '''Indica el final de la aplicacion'''
        mensaje = "----------------------- FIN ----------------------------"
        VistaConsola.imprimir(mensaje)
        op = input()
