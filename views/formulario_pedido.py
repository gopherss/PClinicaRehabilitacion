from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from datetime import date
from random import choice, randint

### Entidades
from models.entidad_pedido import Pedido
from models.entidad_proveedor import Proveedor

pedido = Pedido(numero_pedido='', descripcion='',fecha='',cantidad=0,precio_unitario=0,igv=0,precio_total=0)
proveedor = Proveedor(nombre='', celular='', direccion='')

class FormularioPedido:

    def __init__(self, ventana, id_empleado):
        self.ventana = ventana
        self.codigo = id_empleado

        self.cuadro_principal = LabelFrame(
            self.ventana,
            text='registrar pedido'.title(),
            font=('arial', 15, 'bold'),
            fg='royalblue',padx=10, pady=10
        )
        self.cuadro_principal.pack()

        ### Cuadro uno
        self.cuadro_uno = Label(self.cuadro_principal)
        self.cuadro_uno.pack()

        self.txt_numero_pedido = Label(
            self.cuadro_uno, text='N° Pedido: ',
            font=('arial',10,'bold')
        )
        self.txt_numero_pedido.pack(side=LEFT)

        self.abecedario = 'abcdefghijklmnopqrstuvwxyz'.upper()
        self.letra_1 = choice(self.abecedario)
        self.letra_2 = choice(self.abecedario)
        self.letra_3 = choice(self.abecedario)
        self.letra_4 = choice(self.abecedario)

        self.entrada_numero_pedido = Entry(
            self.cuadro_uno, width=14, state='readonly',
            font=('arial',10,'bold'), justify=CENTER,
            textvariable=IntVar(self.cuadro_uno, 
            value='{}{}{}{}'.format(self.letra_1,self.letra_2,self.letra_3,self.letra_4)+str(randint(10,1000)))
        )
        self.entrada_numero_pedido.pack(side=LEFT)

        self.txt_proveedor = Label(
            self.cuadro_uno, text='Proveedor',
            font=('arial',10,'bold')
        )
        self.txt_proveedor.pack(side=LEFT)

        self.entrada_proveedor = ttk.Combobox(
            self.cuadro_uno, width=14, values=self.listar_proveedor(),
            font=('arial',10,'bold'), state='readonly'
        )
        self.entrada_proveedor.current(0)
        self.entrada_proveedor.pack(side=LEFT)

        self.txt_cantidad = Label(
            self.cuadro_uno, text='Cantidad: ',
            font=('arial',10,'bold')
        )
        self.txt_cantidad.pack(side=LEFT)

        self.entrada_cantidad = Entry(
            self.cuadro_uno, width=14,
            justify=CENTER, textvariable=IntVar(self.cuadro_uno, value=0),
            font=('arial',10,'bold')
        )
        self.entrada_cantidad.bind_all('<Key>', lambda evento : self.calculo_monto_total())
        self.entrada_cantidad.pack(side=LEFT)

        ### Cuadro Dos
        self.cuadro_dos = Label(self.cuadro_principal)
        self.cuadro_dos.pack(padx=10, pady=10)

        self.txt_precio_unitario = Label(
            self.cuadro_dos, text='Precio Unitario: ',
            font=('arial',10,'bold')
        )
        self.txt_precio_unitario.pack(side=LEFT)

        self.entrada_precio_unitario = Entry(
            self.cuadro_dos, textvariable=IntVar(self.cuadro_dos, value=0), 
            font=('arial',10,'bold'), justify=CENTER, width=15
        )
        self.entrada_precio_unitario.pack(side=LEFT)

        self.txt_igv = Label(
            self.cuadro_dos, text='IGV: ',
            font=('arial',10,'bold')
        )
        self.txt_igv.pack(side=LEFT)

        self.entrada_igv = Entry(
            self.cuadro_dos, textvariable=IntVar(self.cuadro_dos, value=0.18),
            font=('arial',10,'bold'), justify=CENTER, width=8
        )
        self.entrada_igv.pack(side=LEFT)


        self.txt_precio_total = Label(
            self.cuadro_dos, text='Precio Total: ',
            font=('arial',10,'bold')
        )
        self.txt_precio_total.pack(side=LEFT)

        self.entrada_precio_total = Label(
            self.cuadro_dos, width=10, fg='seagreen',
            font=('arial',11,'bold'), justify=CENTER, 
            relief=GROOVE, bd=3
        )
        self.entrada_precio_total.pack(side=LEFT)
        
        ### Cuadro Tres
        self.cuadro_tres = Label(self.cuadro_principal)
        self.cuadro_tres.pack(padx=10, pady=10)

        self.txt_descripcion = Label(
            self.cuadro_tres, text='Descripción',
            font=('arial',10,'bold')
        )
        self.txt_descripcion.pack(side=LEFT)

        self.entrada_descripcion = ScrolledText(
            self.cuadro_tres, width=25, height=9, bd=3, relief=GROOVE,
            font=('arial',12,'bold'), fg='royalblue'
        )
        self.entrada_descripcion.pack(side=LEFT)

        self.txt_fecha = Label(
            self.cuadro_tres, text='Fecha',
            font=('arial',10,'bold')
        )
        self.txt_fecha.pack(side=LEFT)

        self.entrada_fecha = Calendar(
            self.cuadro_tres, selectmode='day' ,year=date.today().year,
            month=date.today().month, day=date.today().day
        )
        self.entrada_fecha.pack(side=LEFT)

        ### Mensaje de texto
        self.txt_mensaje = Label(self.cuadro_principal, font=('arial',11,'bold'))
        self.txt_mensaje.pack(pady=5, padx=20)

        ### Cuadro cuatro
        self.cuadro_cuatro = Label(self.cuadro_principal)
        self.cuadro_cuatro.pack(padx=10, pady=10)

        self.btn_borrar = Button(
            self.cuadro_cuatro, text='Borrar', fg='white',
            bg='crimson', padx=30, pady=2,
            command=self.eliminar_pedido
        )
        self.btn_borrar.pack(side=LEFT, padx=10)

        self.btn_editar = Button(
            self.cuadro_cuatro, text='Editar', fg='white',
            bg='darkorange', padx=30, pady=2
        )
        self.btn_editar.pack(side=LEFT, padx=10)

        self.btn_guardar = Button(
            self.cuadro_cuatro, text='Guardar', fg='white',
            bg='dodgerblue', padx=30, pady=2,
            command=self.registrar_pedido
        )
        self.btn_guardar.pack(side=LEFT, padx=10)

        self.tabla_pedido = ttk.Treeview(
            self.cuadro_principal, height=10, columns=(0,1,2,3)
        )
        self.tabla_pedido.heading('#0', text='Descripción')
        self.tabla_pedido.heading('#1', text='Fecha')
        self.tabla_pedido.heading('#2', text='Cantidad')
        self.tabla_pedido.heading('#3', text='Precio Unitario S/')
        self.tabla_pedido.heading('#4', text='Precio Total S/')
        self.tabla_pedido.pack()

        self.buscar_pedido()
    
    def validacion(self):
        return len(self.entrada_numero_pedido.get()) > 0 and \
            len(self.entrada_descripcion.get(1.0, END)) > 1 and \
            self.entrada_precio_unitario.get() != '0' and \
            len(self.entrada_precio_unitario.get()) > 0 and \
            self.entrada_cantidad.get() != '0' and \
            len(self.entrada_cantidad.get()) > 0 and\
            self.entrada_igv.get() != '0' and \
            len(self.entrada_igv.get()) > 0 and \
            self.entrada_precio_total['text'] != '0' and \
            len(str(self.entrada_precio_total['text'])) > 0

    def calculo_monto_total(self):
        try:
            monto_total = pedido.calcular_precio_total(
                cantidad=float(self.entrada_cantidad.get()),
                precio_unitario=float(self.entrada_precio_unitario.get()),
                igv=float(self.entrada_igv.get())
                )
        
            self.entrada_precio_total['text'] = monto_total
        except ValueError:
            pass

 
    def buscar_pedido(self):
        ### Limpiar tabla

        for elemento in self.tabla_pedido.get_children():
            self.tabla_pedido.delete(elemento)

        ### Registrar tabla

        for fila in pedido.obtener_pedido():
            self.tabla_pedido.insert('', 0, text=fila[2], values=(fila[3], round(fila[4]), fila[5], fila[7]), tags=fila[0])
    
    def registrar_pedido(self):
        if self.validacion():
            pass
        else:
            self.txt_mensaje.config(text='Datos Faltantes', fg='crimson')

    def eliminar_pedido(self):
        
        try:
            self.tabla_pedido.item(self.tabla_pedido.selection())['tags'][0]
            
        except IndexError:
            self.txt_mensaje.config(text='Selecciona un pedido', fg='red')
    
    def listar_proveedor(self):
        nombres = list()
        for nombre in proveedor.obtener_proveedor():
            nombres.append(nombre[1])
        return nombres
