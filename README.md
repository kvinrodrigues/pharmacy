# Sistema de Pedidos para Farmacias
Aplicacion para la realizacion de pedidos fisicos dentro de una farmacia 

### Instrucciones para el usuario

   `Pasos previos a la ejecucion del sistema:`
    En caso que no existan articulos persistidos, ejecutar la clase test.py 
    para realizar la inicializacion  con unos datos predefinidos (se crearan articulos para la farmacia)

### Ejecucion: 
    Ejecutar la aplicación desde el archivo aplicacion_consola.py (Sin interfaz grafica) o aplicacion_tkinter.py (Con interfaz grafica) 
    Se mostrará el menú principal con las opciones: 
        "1. Realizar pedido", 
        "2. Cobrar pedido",
        "3. Listar articulos",
        "4. Obtener Informe",
        "0. Salir"
    Se debe insertar la opcion visualizada, pudiendo ser estas (0,1,2,3,4)

  Realizar Pedido: 

    Vista en Consola:
      - Para utilizar dicho menu primeramente debe seleccionar la categoria,
      pudiendose introducir los valores de: (0, 1, 2), entonces se visualizara 
      el listado de articulos seleccionables.
      - Luego debe seleccionar los articulos de manera individual a traves de codigo 
      que precede a la descripcion  del articulo.
      - Puede introducir el valor -2 para volver a seleccionar otras categorias de articulos
      finalmente, para confirmar el pedido, debe introducir el valor -1
      * Se visualizara el detalle de la orden (Dicho valor debe ser utilizado al cobrar el pedido - guarda dicho valor)
  
    Vista Tkinter: 
      Se deberan seleccionar los articulos de manera individual (se podra cambiar de categorias posibles presionando en el numerp identificador de la categoria o en el signo menos que se observa debajo del titulo), presionando en el boton "Lo quiero!" para luego dar click en el boton Finalizar, se obtendra un numero de orden a utilizar para realizar el cobro del pedido.
      * Se visualizara el detalle de la orden (Dicho valor debe ser utilizado al cobrar el pedido - guarda dicho valor)
  
   Cobrar pedido: 
      Vista en Consola:
        - Para realizar el cobro de pedidos creados a traves de ordenes, 
       debe introducir primeramente el numero de orden.
        - Luego debe introducir su numero de cedula (obligatorio), si no existe el cliente. 
        Se podra proceder a la creacion del mismo, si selecciona "N: No" se utilizara un cliente por defecto. 
        - Finalmente debe seleccionar el metodo de pago (Opcion 1: Efectivo, Opcion 2: Tarjeta)
        * Se visualizara el detalle de la factura

      Vista Tkinter:
      Se debera introducir el numero de orden proveido al momento de realizar el pedido, para luego introducir el numero de cedula del cliente. Se podra realizar la creacion de cliente en caso que no exista. Finalmente debe seleccionar el metodo de pago
      * Se visualizara el detalle de la factura
   
      Listar articulos: Se visualizaran los articulos de la farmacia por categoria en las vistas disponibles.

   Obtener Informe: 
     - Vista en Consola: 
        Primeramente se debera seleccionar el periodo de tiempo, pudiendo ser estos: 
        (Opcion DD: Segun el dia a introducir, Opcion WW: Segun el numero de semana del mes introducido, Opcion MM: Segun el mes introducido, Opcion YY: Por anio introducido)
      - Vista Tkinter:
        De acuerdo a lo introducido: 
        Si se introduce nada mas el anio, el informe sera anual. 
        Si se introduce anio y mes, el informe sera mensual.
        Si se introduce anio, mes y dia el informe sera diario.
        Si se introduce anio, mes y semana el informe sera semanal.

  Obs: Borrar archivos comprobantes.pickle, ordenes.pickle, clientes.pickle
## Autor
* **Kevin Rodrigues** - *Desarrollo de la aplicacion* - [Kevin Rodrigues](https://github.com/soykevinrodrigues)       
