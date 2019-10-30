__author__ = "Kevin Samuel Rodrigues Toledo"
''' 
    Sistema de Pedidos en Farmacias

'''
import pickle


class Modelo:
    ''' Controla las creaciones, modificaciones y busquedas entre los objetos
                persistidos '''

    def crear(self, directorio, objeto):
        ''' Creación de objeto'''
        if (objeto is not None):
        	archivo = open(directorio + '.pickle', 'wb')
        	pickle.dump(objeto, archivo)
        	archivo.close()

    def buscar(self, directorio):            
        archivo = open(directorio + '.pickle', 'rb')
        objeto = pickle.load(archivo)
        archivo.close()
        return objeto
