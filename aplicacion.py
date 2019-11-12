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
        vista = Vista()
        # TODO poner cada opcion disponible en un diccionario que contenga una tupla (titulo, accion)
        while(True):
            opcion_menu = Vista.menu_principal()
            if opcion_menu == 0:
                Aplicacion.salir()
            elif opcion_menu == 1:
                Vista.realizar_pedido()
            elif opcion_menu == 2:
                Vista.cobrar_pedido()
            elif opcion_menu == 3:
                vista.desplegar_articulos()
            elif opcion_menu == 4:
                pass
            else:
                Vista.error_menu()
                Vista.pausa()

            Controlador.guardar_nuevos_datos(Controlador.farmacia)


if __name__ == '__main__':
    Aplicacion.main()
