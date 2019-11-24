from tkinter import *


class VistaTkinter:
    @staticmethod
    def agregar_espaciado(ventana_raiz):
        (Etiqueta(ventana=ventana_raiz.ventana,
                  nombre="", color="black",
                  fuente='Arial', tamano=6)).invocar_pack()

    @staticmethod
    def menu_principal():
        ''' Metodo para el menu principal de la aplicacion '''
        vista_principal = Ventana('Principal')

        ventana_raiz = VTopLevel(
            vista_principal, "Sistema de pedidos para farmacias")
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
                                   evento=lambda: print('asdasd'))

        boton_hacer_pedido.invocar_pack()
        boton_hacer_pedido.boton.configure(width=15)

        VistaTkinter.agregar_espaciado(ventana_raiz)

        boton5 = Boton(ventana=ventana_raiz.ventana,
                       nombre="Salir", color="white",
                       evento=lambda: VistaTkinter.cerrar_aplicacion(
                           ventana_raiz, vista_principal))
        boton5.invocar_pack()
        boton5.boton.configure(background='red', width=15)
        vista_principal.invocar()

    @staticmethod
    def cerrar_aplicacion(ventana_raiz, vista_principal):
        ''' Metodo para salir de la aplicación '''
        ventana_raiz.ventana.withdraw()
        ventana1 = VTopLevel(ventana_raiz.ventana, "Salir del Sistema")
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
        self.ventana = Toplevel()
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
