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
        datos = Controlador.inicializar()
        Menu.menu_principal(datos)

    @staticmethod
    def salir():
        '''Cierra la aplicación'''
        Vista.limpiar_pantalla()
        Vista.cerrar_aplicacion()        
class Menu:
    @staticmethod
    def menu_principal(datos):
        ''' Metodo que contiene la parte funcional del menu principal de la aplicación '''
        while(True):
            # datos[0] = ordenes
            # datos[1] = clientes
            # datos[2] = empleados
            # datos[3] = comprobantes
            # datos[4] = articulos
            # datos[5] = farmacia
            # TODO descomentar Vista.limpiar_pantalla()
            opcion_menu = Vista.menu_principal()
            if opcion_menu == 0:
                Aplicacion.salir()
            elif opcion_menu == 1:
                pass
            elif opcion_menu == 2:
                pass
            elif opcion_menu == 3:
                pass
            elif opcion_menu == 4:
                datos[5].listar_articulos()
            else:
                Vista.error_menu()
                Vista.pausa()

            Controlador.guardar_nuevos_datos(
                datos[0], datos[1], datos[3], datos[4])


if __name__ == '__main__':
    Aplicacion.main()
