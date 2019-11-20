# ------------------------ Constantes ------------------------

# Tipos de Documentos
documento_orden = 'ORDEN'

# Tipos de Articulos

key_medicamento = 0
key_higiene = 1
key_belleza = 2

categoria_articulos = {
    key_medicamento: 'medicamento',
    key_higiene: 'higiene',
    key_belleza: 'belleza'
}

# Informacion basica de la empresa
business_name = 'FarmaService'
business_ruc = '45465465-12'

# Estados de ordenes
estado_pendiente = 'PENDIENTE'
estado_pagado = 'PAGADO'

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
        TODO documentar mejor
    '''
    accion()

