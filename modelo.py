__author__ = "Kevin Samuel Rodrigues Toledo"
''' 
    Sistema de Pedidos en Farmacias

'''
import pickle


class Modelo:
    ''' Controla las creaciones, modificaciones y busquedas entre los objetos
                persistidos '''
    
    def crear(self, directorio, objeto, extension = '.pickle'):
        ''' Creación de objeto'''
        if (objeto is not None):
        	archivo = open(directorio + extension, 'wb')
        	pickle.dump(objeto, archivo)
        	archivo.close()

    def buscar(self, directorio, extension = '.pickle'):
        ''' Busqueda de objeto '''             
        archivo = open(directorio + extension, 'rb')
        objeto = pickle.load(archivo)
        archivo.close()
        return objeto
