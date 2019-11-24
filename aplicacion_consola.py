__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

from controlador import *
from clases import *
from vista_consola import *

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
        Vista_Consola.limpiar_pantalla()
        Vista_Consola.cerrar_aplicacion()


class Menu:
    ''' Clase que contiene el menu principal '''
    @staticmethod
    def menu_principal():
        ''' Metodo que contiene la parte funcional del menu principal de la aplicación '''
        menus = {0: ('Salir', lambda: Aplicacion.salir()),
                 1: ('Realizar pedido', lambda: Vista_Consola.realizar_pedido()),
                 2: ('Cobrar Pedido', lambda: Vista_Consola.cobrar_pedido()),
                 3: ('Listar Articulos', lambda: Vista_Consola.desplegar_articulos()),
                 4: ('Gestionar Informe', lambda: Vista_Consola.gestionar_informe())
                 }

        while(True):
            opcion_menu = Vista_Consola.menu_principal()
            try:
                opcion = menus[opcion_menu]
                utiles.realizar(opcion[1])
            except KeyError:
                Vista_Consola.error_menu()
                Vista_Consola.pausa()

            Controlador.guardar_nuevos_datos(Controlador.farmacia)


if __name__ == '__main__':
    Aplicacion.main()
