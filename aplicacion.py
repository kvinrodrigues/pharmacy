__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "0.0.1"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

from controlador import *
from clases import *
from vista import *


class Aplicacion:
    '''Clase destinada a la ejecucion de la aplicacion'''

    @staticmethod
    def main():
        '''Punto de inicio del programa'''
        Controlador.inicializar()
        Menu.menu_principal()

    @staticmethod
    def salir():
        '''Cierra la aplicación'''
        Vista.limpiar_pantalla()
        Vista.cerrar_aplicacion()


class Menu:
    @staticmethod
    def menu_principal():
        ''' Metodo que contiene la parte funcional del menu principal de la aplicación '''
        menus = {0: ('Salir', lambda: Aplicacion.salir()), 1: ('Realizar pedido', lambda: Vista.realizar_pedido()),
                 2: ('Cobrar Pedido', lambda: Vista.cobrar_pedido()), 3 : ('Listar Articulos', lambda: Vista.desplegar_articulos())}

        while(True):
            opcion_menu = Vista.menu_principal()
            try: 
                opcion = menus[opcion_menu]
                opcion[1]()
            except KeyError:
                Vista.error_menu()
                Vista.pausa()

            # TODO: guardar cada vez que se realicen creaciones en la farmacia
            Controlador.guardar_nuevos_datos(Controlador.farmacia)


if __name__ == '__main__':
    Aplicacion.main()
