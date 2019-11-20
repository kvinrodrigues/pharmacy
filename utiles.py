__author__ = "Kevin Samuel Rodrigues Toledo"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "kevin.rodrigues@fpuna.edu.py"
__status__ = "Prototype"

'''
    Sistema de Pedidos en Farmacias
    Este script contiene los elementos comunes utilizados a lo largo del sistema
'''

# ------------------------ Constantes ------------------------

# Tipos de Documentos
DOCUMENTO_ORDEN = 'ORDEN'
NUMERO_DOC_ORDEN = 0

# Tipos de Articulos

KEY_MEDICAMENTO = 0
KEY_HIGIENE = 1
KEY_BELLEZA = 2

CATEGORIA_ARTICULOS = {
    KEY_MEDICAMENTO: 'medicamento',
    KEY_HIGIENE: 'higiene',
    KEY_BELLEZA: 'belleza'
}

# Informacion basica de la empresa
NOMBRE_EMPRESA = 'FarmaService'
RUC_EMPRESA = '45465465-12'

# Estados de ordenes
ESTADO_PENDIENTE = 'PENDIENTE'
ESTADO_PAGADO = 'PAGADO'

# Datos cliente por defecto
CLIENTE_DEFECTO_NOMBRE = 'ElSEIS'
CLIENTE_DEFECTO_APELLIDO = 'MIL'
CLIENTE_DEFECTO_DIRECCION = 'Asuncion c/Identificaciones'
CLIENTE_DEFECTO_CONTACTO_VALOR = 'elseis_mil@correo.com'
CLIENTE_DEFECTO_CI = '6000'
CLIENTE_DEFECTO_RUC = '6000-1'



# ------------------------ Metodos comunes ------------------------

def realizar(accion):
    ''' 
        Metodo que recibe una accion a realizar (debe recibir una funcion)
    '''
    accion()

