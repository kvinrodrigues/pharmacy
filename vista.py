from controlador import *
import os
import sys
import logging
import constants

logging.basicConfig(level=logging.DEBUG)


class Vista:
    controlador = Controlador()

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
    def salir():
        '''Confirmación para salir'''
        op = input("Presione enter para salir. ")
        return

    @staticmethod
    def pausa():
        '''Confirmación para continuar'''
        entrada = input("Continuar... ")
        return

    @staticmethod
    def final():
        '''Indica el final de la aplicacion'''
        mensaje = "----------------------- FIN ----------------------------"
        Vista.imprimir(mensaje)
        op = input()

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
                   + "2. Pagar pedido \n"
                   + "3. Obtener informe \n"
                   + "4. Listar Articulos \n"
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
        Vista.imprimir('Aqui debe imprimir las categorias y su codigo correspondiente!')
        pass

    @staticmethod
    def seleccionar_articulos():
        articulos_categorizados = Controlador.filtrar_articulos()
        mensaje = ("--------- Seleccione categoria del articulo ---------")
        Vista.imprimir(mensaje)
        Vista.imprimir_opciones_categorias()
        categoria_seleccionada = Vista.seleccionar_categoria() # TODO validar que sea valida quizas a traves de KeyError
        articulos_correspondientes = articulos_categorizados[categoria_seleccionada]
        # TODO separar
        Vista.limpiar_pantalla()
        Vista.imprimir('Articulos de la categoria: ' + str(categoria_seleccionada))
        for articulo in articulos_correspondientes:
            Vista.imprimir(articulo)
        Vista.imprimir('Ingrese numero de articulos, enter para confirmar.')
        Vista.imprimir('Ingrese numero de articulo -1 para terminar')
        articulos = Vista.seleccionar_articulos_desde(articulos_correspondientes)
        return articulos

    @staticmethod
    def seleccionar_articulos_desde(articulo_en_categoria):
        articulos = []
        entrada = Vista.leer_cadena()
        # TODO Analizar para optimizar, puede ser cuadratico lo sgte
        # TODO ver otra forma de hacer sin el while
        while(not entrada[0] == '-1'):
            articulo = Controlador.filtrar_articulo_desde(articulo_en_categoria, entrada)
            if articulo is not None:
                articulos.append(articulo)
            else:    
                Vista.imprimir('No se pudo agregar el articulo ingresado.')
            entrada = Vista.leer_cadena()
        return articulos    

    @staticmethod
    def realizar_pedido():
        articulos = Vista.seleccionar_articulos()
        orden = Controlador.crear_orden(articulos)
        # TODO cambiar impresion
        Vista.imprimir('Orden creada: ' + str(orden.numero_orden))
        Vista.pausa()

    def desplegar_articulos(self):
        articulos_categorizados = self.controlador.filtrar_articulos()
        '''
            El parametro <<articulos_categorizados>> recibido, es un DICCIONARIO que posee los articulos disponibles en categoria
        '''
        articulos_higiene = articulos_categorizados[constants.tipo_higiene[0]]
        articulos_medicamento = articulos_categorizados[constants.tipo_medicamento[0]]
        articulos_belleza = articulos_categorizados[constants.tipo_belleza[0]]
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

    @staticmethod
    def imprimir(mensaje):
        ''' Mediante este metodo se imprime en la consola
        '''
        print(mensaje)
