from vista import *
import logging
from controlador import *
'''
Realizacion de pruebas temporales
'''
logging.basicConfig(level=logging.DEBUG)
vista = Vista()
controlador = Controlador()
modelo = Modelo()

# Happy Cases


def test_success_input_number():
    numero = vista.leer_numero("Introduzca numero: ", 0, 150000, 2)
    logging.debug('Se introdujo el valor: ' + str(numero))


def test_success_input_string():
    texto = vista.leer_cadena("Introduzca mensaje: ", 'defaultValue')
    logging.debug('Se introdujo el valor: ' + texto[0])


def test_menu_principal():
    Vista.menu_principal()

# Controlador
# TODO agregar tambien los demas datos necesarios
def test_guardar_nuevo_dato():
    list_articulos = [Medicamento('0000', 'Omeprazol', 12000, 200), Medicamento('0001', 'Supradyn', 23500, 121), 
    Belleza('0003','Shampu', 35000, 50), Belleza('0004', 'Colageno', 40000, 45), Higiene('0005', 'Jabon', 5400, 140), 
    Higiene('0006', 'Pasta Dental', 10000, 45)]
    farmacia = Farmacia(list_articulos, utiles.business_name, utiles.business_ruc)
    controlador.guardar_nuevos_datos(farmacia)
    
# Modelo       
def test_buscar_articulos():
    articulos = modelo.buscar('datos_articulos/articulos')
    for articulo in articulos:
        print(articulo.descripcion)

def test_exit():
    vista.cerrar_aplicacion()



if __name__ == "__main__":
    # Se limpia la pantalla con el metodo proveido
    vista.limpiar_pantalla()
    logging.debug('Se limpio la pantalla...')

    logging.debug('Ejecutando pruebas de la aplicacion')
    # test_success_input_number()
    # test_success_input_string()
    # test_menu_principal()
    test_guardar_nuevo_dato()
    # test_buscar_articulos()

    logging.info("Everything passed")
    test_exit()
    
