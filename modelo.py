__author__ = "Kevin Samuel Rodrigues Toledo"
''' 
    Sistema de Pedidos en Farmacias

'''
import pickle

class Modelo:
    ''' Controla las creaciones, modificaciones y busquedas entre los objetos
        persistidos 
    '''
    
    def crear(self, directorio, objeto, extension = '.pickle'):
        ''' Metodo para realizar la serializacion en el archivo'''
        if (objeto is not None):
        	archivo = open(directorio + extension, 'wb')
        	pickle.dump(objeto, archivo)
        	archivo.close()

    def buscar(self, directorio, extension = '.pickle'):
        ''' Busqueda de objeto '''
        no_encontrado = 'No encontrado'
        try:   
            archivo = open(directorio + extension, 'rb')
            objeto = pickle.load(archivo)
            archivo.close()
            return objeto
        except IOError:
            return no_encontrado