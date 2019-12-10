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
        VistaConsola.limpiar_pantalla()
        VistaConsola.cerrar_aplicacion()


class Menu:
    ''' Clase que contiene el menu principal '''
    @staticmethod
    def menu_principal():
        ''' Metodo que contiene la parte funcional del menu principal de la aplicación '''
        menus = {0: ('Salir', lambda: Aplicacion.salir()),
                 1: ('Realizar pedido', lambda: VistaConsola.realizar_pedido()),
                 2: ('Cobrar Pedido', lambda: VistaConsola.cobrar_pedido()),
                 3: ('Listar Articulos', lambda: VistaConsola.desplegar_articulos()),
                 4: ('Gestionar Informe', lambda: VistaConsola.gestionar_informe())
                 }

        while(True):
            opcion_menu = VistaConsola.menu_principal()
            try:
                opcion = menus[opcion_menu]
                utiles.realizar(opcion[1])
            except KeyError:
                VistaConsola.error_menu()
                VistaConsola.pausa()

            Controlador.guardar_nuevos_datos(Controlador.farmacia)


if __name__ == '__main__':
    Aplicacion.main()
