from controlador import *
import os
import sys
import logging
import constants

logging.basicConfig(level=logging.DEBUG)


class Vista:
    controlador = Controlador()

    @staticmethod
    def realizar_pedido():
        try:
            articulos = []
            articulos = Vista.seleccionar_articulos(articulos)
            if articulos:
                orden = Controlador.crear_orden(articulos)
                Vista.imprimir('Orden creada: ' + str(orden.numero_orden))
                for art in articulos:
                    Vista.imprimir(art.descripcion)
            else:
                Vista.imprimir('Debe introducir por lo menos un articulo.')    
        except Exception:
            Vista.imprimir('No se pudo generar la orden...')
        Vista.pausa()

    @staticmethod
    def cobrar_pedido():
        # Se ingres el numero de orden
        # Luego se verifica su validez, si
        # no es valido se lanza una excepcion(no se encuentra contemplado tal caso en las especificaciones)

        entrada = Vista.leer_numero()
        try:
            orden = Controlador.buscar_orden(entrada)
            cliente = Cliente(Persona(Contacto(), 'asdasd', 'Prueba',
                                  'Prueba', 'st. tu casa', '111'))  # TODO cambiar
            # TODO se debe poder seleccionar el medio de pago
            medio_pago = MedioPago(
                'Efectivo', 'Valor monetario mediante billetes y monedas')
            comprobante = Controlador.crear_comprobante(orden, medio_pago, cliente)
            Controlador.guardar_comprobante(comprobante)
        except Exception as e:
            Vista.imprimir('No se pudo realizar el cobro: ' + str(e))
        Vista.pausa() 

    @staticmethod
    def desplegar_articulos():
        Vista.limpiar_pantalla()
        Vista.imprimir('---------- Listado de Articulos en categoria ----------')
        articulos_categorizados = Controlador.filtrar_articulos() # DICCIONARIO que posee los articulos disponibles en categoria
        articulos_higiene = articulos_categorizados[constants.key_higiene]
        articulos_medicamento = articulos_categorizados[constants.key_medicamento]
        articulos_belleza = articulos_categorizados[constants.key_belleza]
        # TODO separar esta parte, debe estar en el controlador...
        # Debe ser una excepcion capturada por la vista
        condicion = (len(articulos_higiene) == 0 and len(articulos_medicamento)
                     and len(articulos_belleza) == 0)
        if condicion:
            Vista.farmacia_sin_articulos()
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
            Vista.imprimir(mensaje)
            Vista.pausa()

    # Metodo para limpiar la pantalla
    @staticmethod
    def limpiar_pantalla():
        '''Limpia la pantalla de la sesion utilizada'''
        os.system('cls' if os.name == 'nt' else 'clear')

    # Metodo para la lectura de numeros con manejo de excepciones
    @staticmethod
    def leer_numero(mensaje='', valor_minimo=0, valor_maximo=None, default=None):
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
            return ("Debe ingresar un número")
        except TypeError as e:
            return ("Debe ingresar un número")
        except Exception as e:
            return (e)

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
        Vista.imprimir(mensaje)

    @staticmethod
    def menu_principal():
        ''' Vista del menú principal'''
        Vista.limpiar_pantalla()
        mensaje = ("---------------- Bienvenido al Sistema de Pedidos para Farmacias ---------------\n" +
                   "------------------- Menú Principal ----------------- \n" +
                   "Ingrese el número correspondiente a la opción deseada: \n"
                   + "1. Realizar pedido \n"
                   + "2. Cobrar pedido \n"
                   + "3. Listar Articulos \n"
                   + "4. Obtener informe \n"
                   + "0. Salir")
        Vista.imprimir(mensaje)

        while(True):
            Vista.imprimir("Accion: ")
            opcion_menu = Vista.leer_numero()
            if isinstance(opcion_menu, str):
                Vista.imprimir(opcion_menu)
            else:
                break

        return opcion_menu

    @staticmethod
    def cerrar_aplicacion():
        '''Confirmación para cerrar la aplicación'''
        mensaje = ("--------------- Cerrar aplicación ----------------\n" +
                   "\n Está Seguro? \t\tSí = 1 \t\tNo = 0 ")
        Vista.imprimir(mensaje)
        entrada = Vista.leer_numero('Confirme: ', 0, 1, 0)
        if (entrada == 1):
            sys.exit()

    @staticmethod
    def farmacia_sin_articulos():
        '''Mensaje de Farmacia sin articulos'''
        mensaje = ("---------------- FARMACIA FUERA DE STOCK ---------------\n" +
                   "Por favor, regrese mas tarde.")
        Vista.imprimir(mensaje)

    @staticmethod
    def seleccionar_categoria():
        return Vista.leer_numero("Ingrese categoria: ")

    @staticmethod
    def imprimir_opciones_categorias():
        # TODO implementar
        mensaje = (
            '------------------- Categorias Disponibles ----------------------------')
        categorias = Controlador.obtener_categorias_articulos()
        for id in categorias:
            mensaje += '\n'
            mensaje += str(id) + '- ' + \
                Controlador.obtener_nombre_categoria(id)
        mensaje += '\n'
        mensaje += '-----------------------------------------------------------------------'
        Vista.imprimir(mensaje)

    @staticmethod
    def seleccionar_articulos(articulos_seleccionados):
        Vista.limpiar_pantalla()
        mensaje = ("--------- Seleccione categoria del articulo ---------")
        Vista.imprimir(mensaje)
        Vista.imprimir_opciones_categorias()
        categoria_seleccionada = Vista.seleccionar_categoria()
        try:
            articulos_en_categoria = Controlador.obtener_articulos_por_categoria(
                categoria_seleccionada)
            Vista.limpiar_pantalla()
            Vista.imprimir('Articulos de la categoria: ' +
                           str(categoria_seleccionada))
            for articulo in articulos_en_categoria:
                Vista.imprimir(articulo)
            Vista.imprimir(
                'Ingrese identificadores de los articulos, enter para confirmar.')
            Vista.imprimir('Ingrese numero de articulo -1 para terminar')
            articulos_parciales = Vista.seleccionar_articulos_desde(
                articulos_en_categoria)
            articulos_seleccionados.extend(articulos_parciales)    
            return articulos_seleccionados

        except Exception as e:
            Vista.imprimir(e)
            raise e

    @staticmethod
    def seleccionar_articulos_desde(articulo_en_categoria):
        articulos = []
        entrada = Vista.leer_cadena()
        while(not entrada[0] == '-1'):
            if entrada[0] == '-2':
                Vista.seleccionar_articulos(articulos)
                break
            articulo = Controlador.filtrar_articulo_desde(
                articulo_en_categoria, entrada[0])
            if articulo is not None:
                articulos.append(articulo)
            else:
                Vista.imprimir('No se pudo agregar el articulo ingresado.')
            entrada = Vista.leer_cadena()
        return articulos

    @staticmethod
    def imprimir(mensaje):
        ''' Mediante este metodo se imprime en la consola
        '''
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
        Vista.imprimir(mensaje)
        op = input()
