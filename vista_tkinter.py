from tkinter import *
import tkinter as tk
from controlador import *


class VistaTkinter:

    @staticmethod
    def realizar_pedido(ventana_raiz):
        articulos = VistaTkinter.seleccionar_articulos(ventana_raiz)
        if articulos:
            orden = Controlador.crear_orden(articulos)
            # TODO mostrar mensaje de creacion de orden
        else:
            # raise Exception('Debe introducir por lo menos un articulo.')
            pass

    @staticmethod
    def seleccionar_articulos(ventana_raiz):
        ventana_hija = VTopLevel(ventana_raiz.ventana, '')
        ventana_hija.ventana.geometry("350x470+500+200")
        ventana_hija.ventana.configure(background='white')
        etiqueta_titulo = Etiqueta(ventana=ventana_hija.ventana,
                                   nombre="Realizar Pedido", color="#0078D7",
                                   fuente='Verdana', tamano=16)
        etiqueta_seleccion = Etiqueta(ventana=ventana_hija.ventana,
                                      nombre="Categoria: ", color="#0078D7",
                                      fuente='Verdana', tamano=10)
        etiqueta_titulo.invocar_pack()
        etiqueta_seleccion.invocar_pack()
        option_list = Controlador.obtener_categorias_articulos()
        # TODO crear clases propias para String var y optionmenu
        variable = tk.StringVar(ventana_hija.ventana)
        variable.set(option_list[0])
        opt = tk.OptionMenu(ventana_hija.ventana, variable, *option_list)
        opt.config(width=90, font=('Verdana', 12))
        opt.pack(side="top")

        etiqueta_categoria = Etiqueta(ventana=ventana_hija.ventana,
                                      nombre=Controlador.obtener_nombre_categoria(int(variable.get())), color="#0078D7",
                                      fuente='Verdana', tamano=16)
        etiqueta_categoria.invocar_pack()

        def callback(*args):
            categoria_seleccionada = Controlador.obtener_nombre_categoria(int(variable.get()))
            etiqueta_categoria.etiqueta.configure(text="{}".format(categoria_seleccionada))

        variable.trace("w", callback)

    @staticmethod
    def desplegar_articulos(ventana_raiz):
        articulos_categorizados = Controlador.filtrar_articulos()
        articulos_higiene = articulos_categorizados[utiles.KEY_HIGIENE]

        articulos_medicamento = articulos_categorizados[utiles.KEY_MEDICAMENTO]
        articulos_belleza = articulos_categorizados[utiles.KEY_BELLEZA]
        if not Controlador.farmacia_existen_articulos():
            mensaje = "Farmacia sin articulos"
        else:
            mensaje = ('--- MEDICAMENTOS: --- \n')
            for medicamento in articulos_medicamento:
                mensaje = (mensaje + medicamento.descripcion + '\n')

            mensaje = mensaje + ('--- ARTICULOS DE HIGIENE PERSONAL: --- \n')
            for higiene in articulos_higiene:
                mensaje = (mensaje + higiene.descripcion + '\n')

            mensaje = mensaje + ('--- ARTICULOS DE BELLEZA: --- \n')
            for belleza in articulos_belleza:
                mensaje = (mensaje + belleza.descripcion + '\n')

        ventana_raiz.ventana.withdraw()

        ventana1 = VTopLevel(ventana_raiz.ventana, 'Articulos Disponibles')
        ventana1.ventana.geometry("350x470+500+200")
        ventana1.ventana.configure(background='white')

        etiqueta1 = Etiqueta(ventana=ventana1.ventana,
                             nombre="Articulos Disponibles", color="#0078D7",
                             fuente='Verdana', tamano=16)
        etiqueta1.invocar_pack()

        etiqueta2 = Etiqueta(ventana=ventana1.ventana,
                             nombre=mensaje, color="black",
                             fuente='Verdana', tamano=10)
        etiqueta2.invocar_pack()

        boton1 = Boton(ventana=ventana1.ventana,
                       nombre="OK", color="white",
                       evento=lambda: ventana1.salir()
                                      or ventana_raiz.ventana.deiconify())
        boton1.invocar_pack("centro")
        boton1.boton.configure(background="#3687DC", width=9)

    @staticmethod
    def agregar_espaciado(ventana_raiz):
        (Etiqueta(ventana=ventana_raiz.ventana,
                  nombre="", color="black",
                  fuente='Arial', tamano=6)).invocar_pack()

    @staticmethod
    def menu_principal():
        ''' Metodo para el menu principal de la aplicacion '''
        vista_principal = Ventana('Principal')

        ventana_raiz = VTopLevel(vista_principal.ventana, 'Sistema de pedidos para farmacias')
        ventana_raiz.ventana.geometry("384x320+500+200")
        ventana_raiz.ventana.configure(background="white")

        VistaTkinter.agregar_espaciado(ventana_raiz)

        etiqueta2 = Etiqueta(ventana=ventana_raiz.ventana,
                             nombre="Menú Principal", color="#0078D7",
                             fuente='Verdana', tamano=16)
        etiqueta2.invocar_pack()

        VistaTkinter.agregar_espaciado(ventana_raiz)

        boton_hacer_pedido = Boton(ventana=ventana_raiz.ventana,
                                   nombre="Realizar pedido", color="black",
                                   evento=lambda: VistaTkinter.realizar_pedido(ventana_raiz))

        boton_hacer_pedido.invocar_pack()
        boton_hacer_pedido.boton.configure(width=15)

        VistaTkinter.agregar_espaciado(ventana_raiz)

        boton_ver_articulos = Boton(ventana=ventana_raiz.ventana,
                                    nombre="Listar Articulos", color="black",
                                    evento=lambda: VistaTkinter.desplegar_articulos(ventana_raiz))

        boton_ver_articulos.invocar_pack()
        boton_ver_articulos.boton.configure(width=15)

        VistaTkinter.agregar_espaciado(ventana_raiz)

        boton_salir = Boton(ventana=ventana_raiz.ventana,
                            nombre="Salir", color="white",
                            evento=lambda: VistaTkinter.cerrar_aplicacion(
                                ventana_raiz))
        boton_salir.invocar_pack()
        boton_salir.boton.configure(background='red', width=15)
        vista_principal.invocar()

    @staticmethod
    def cerrar_aplicacion(ventana_raiz):
        ''' Metodo para salir de la aplicación '''
        ventana_raiz.ventana.withdraw()
        ventana1 = VTopLevel(ventana_raiz.ventana, 'Salir del Sistema')
        ventana1.ventana.geometry("280x93+500+200")
        ventana1.ventana.configure(background="white")

        VistaTkinter.agregar_espaciado(ventana_raiz)

        etiqueta2 = Etiqueta(ventana=ventana1.ventana,
                             nombre="Seguro que desea salir?", color="black",
                             fuente='Arial', tamano=10)
        etiqueta2.invocar_pack()

        VistaTkinter.agregar_espaciado(ventana_raiz)

        boton1 = Boton(ventana=ventana1.ventana,
                       nombre="Sí", color="white",
                       evento=lambda: ventana1.salir()
                                      or ventana_raiz.salir()
                                      # or vista_principal.destroy()
                                      or sys.exit())
        boton1.invocar_pack("derecha")
        boton1.boton.configure(background='red', width=5)

        boton2 = Boton(ventana=ventana1.ventana,
                       nombre="No", color="black",
                       evento=lambda: ventana1.salir()
                                      or ventana_raiz.ventana.deiconify())
        boton2.invocar_pack("izquierda")
        boton2.boton.configure(width=5)


class Ventana():
    ''' Clase que representa una ventana en la app de escritorio '''

    def __init__(self, nombre):
        self.ventana = Tk()
        # self.ventana.withdraw()
        self.ventana.title(nombre)

    def invocar(self):
        self.ventana.mainloop()

    def salir(self):
        self.ventana.destroy()


class VTopLevel(Ventana):
    '''     Clase que representa la ventana tipo TopLevel, y hereda de Ventana'''

    def __init__(self, master, nombre):
        self.ventana = Toplevel(master=master)
        self.ventana.title(nombre)

    def invocar_pack(self, posicion="centro"):
        if posicion == "centro":
            self.ventana.pack()
        elif posicion == "derecha":
            self.ventana.pack(side=RIGHT)
        elif posicion == "izquierda":
            self.ventana.pack(side=LEFT)


class Boton():
    ''' Clase que representa un botón de Tkinter (Button)'''

    def __init__(self, ventana, nombre, color, evento):
        self.boton = Button(ventana, text=nombre,
                            fg=color, command=evento,
                            cursor="hand2", relief="flat", background="#AAEDED")

    def invocar_place(self, pos_x=100, pos_y=100):
        self.boton.place(x=pos_x, y=pos_y)

    def invocar_grid(self, fila=0, columna=0, comb_fila=1, comb_columna=1):
        self.boton.grid(row=fila, column=columna,
                        rowspan=comb_fila, columnspan=comb_columna)

    def invocar_pack(self, posicion="centro"):
        if posicion == "centro":
            self.boton.pack()
        elif posicion == "derecha":
            self.boton.pack(side=RIGHT)
        elif posicion == "izquierda":
            self.boton.pack(side=LEFT)


class BotonOpcion():
    ''' Clase que representa botón de opción única de Tkinter(RadioButton)'''

    def __init__(self, ventana, nombre, valor, variable):
        self.BotonOpcion = Radiobutton(ventana, text=nombre,
                                       value=valor, variable=variable,
                                       cursor="hand2", background="white")

    def invocar_place(self, pos_x=100, pos_y=100):
        self.BotonOpcion.place(x=pos_x, y=pos_y)

    def invocar_grid(self, fila=0, columna=0, comb_fila=1, comb_columna=1):
        self.BotonOpcion.grid(row=fila, column=columna,
                              rowspan=comb_fila, columnspan=comb_columna)

    def invocar_pack(self, posicion="centro"):
        if posicion == "centro":
            self.BotonOpcion.pack()
        elif posicion == "derecha":
            self.BotonOpcion.pack(side=RIGHT)
        elif posicion == "izquierda":
            self.BotonOpcion.pack(side=LEFT)


class Etiqueta():
    '''     Clase que representa las etiquetas de Tkinter (Label) '''

    def __init__(self, ventana, nombre, color, fuente, tamano):
        self.etiqueta = Label(ventana, text=nombre,
                              fg=color, font=(fuente, tamano), background="white")

    def invocar_place(self, pos_x=100, pos_y=100):
        self.etiqueta.place(x=pos_x, y=pos_y)

    def invocar_grid(self, fila=0, columna=0, comb_fila=1, comb_columna=1):
        self.etiqueta.grid(row=fila, column=columna,
                           rowspan=comb_fila, columnspan=comb_columna)

    def invocar_pack(self, posicion="centro"):
        if posicion == "centro":
            self.etiqueta.pack()
        elif posicion == "derecha":
            self.etiqueta.pack(side=RIGHT)
        elif posicion == "izquierda":
            self.etiqueta.pack(side=LEFT)
