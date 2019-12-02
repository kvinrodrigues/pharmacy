__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

''' 
    Sistema de Pedidos en Farmacias

'''

import pickle


class Modelo:
    ''' Controla las creaciones, modificaciones y busquedas entre los objetos
        persistidos 
    '''

    def crear(self, directorio, objeto, extension='.pickle'):
        ''' Metodo para realizar la serializacion en el archivo'''
        if (objeto is not None):
            archivo = open(directorio + extension, 'wb')
            pickle.dump(objeto, archivo)
            archivo.close()

    def buscar(self, directorio, extension='.pickle'):
        ''' Busqueda de objeto '''
        no_encontrado = 'No encontrado'
        try:
            archivo = open(directorio + extension, 'rb')
            objeto = pickle.load(archivo)
            archivo.close()
            return objeto
        except IOError:
            return no_encontrado
