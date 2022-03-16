from tkinter import *
from tkinter import ttk, messagebox

from models.entidad_proveedor import Proveedor

proveedor = Proveedor('','','')

class FormularioProveedor:
    
    def __init__(self,ventana):
        self.ventana = ventana

        self.cuadro_principal = LabelFrame(
            self.ventana,
            text='registrar proveedor'.title(),
            fg='royalblue',
            font=('consolas',15,'bold'),
            padx=10,pady=10
        )
        self.cuadro_principal.pack()
        
        ### cuadro uno
        self.cuadro_uno = Label(self.cuadro_principal)
        self.cuadro_uno.pack()

        self.txt_nombre = Label(
            self.cuadro_uno,
            text='Nombre:   ',
            font=('arial',10,'bold')
        )
        self.txt_nombre.pack(side=LEFT)

        self.entrada_nombre = Entry(
            self.cuadro_uno, width=30, bd=3,
            font=('arial',10,'bold')
        )
        self.entrada_nombre.pack(side=LEFT)

        ### cuadro dos
        self.cuadro_dos = Label(self.cuadro_principal)
        self.cuadro_dos.pack()

        self.txt_celular = Label(
            self.cuadro_dos,
            text='Celular:    ',
            font=('arial',10,'bold')
        )
        self.txt_celular.pack(side=LEFT)
        
        self.entrada_celular = Entry(
            self.cuadro_dos, justify=CENTER,bd=3,
            font=('arial',10,'bold'),width=30
        )
        self.entrada_celular.pack(side=LEFT)

        ### cuadro tres
        self.cuadro_tres = Label(self.cuadro_principal)
        self.cuadro_tres.pack()

        self.txt_direccion = Label(
            self.cuadro_tres,
            text='Direccion: ',
            font=('arial',10,'bold')
        )
        self.txt_direccion.pack(side=LEFT)

        self.entrada_direccion = Entry(
            self.cuadro_tres, width=30, bd=3,
            font=('arial',10,'bold')
        )
        self.entrada_direccion.pack(side=LEFT)

        ### mensaje de error
        self.txt_mensaje = Label(
            self.cuadro_principal,
            font=('arial', 12, 'bold')
        )
        self.txt_mensaje.pack(pady=10, padx=10)

        ### cuadro cuatro
        self.cuadro_cuatro = Label(self.cuadro_principal)
        self.cuadro_cuatro.pack()

        self.btn_borrar = Button(
            self.cuadro_cuatro,
            text='Borrar', bg='crimson', fg='white',
            font=('consolas',10,'bold'), padx=20, pady=5,
            command=self.eliminar_proveedor
        )
        self.btn_borrar.pack(side=LEFT, padx=10)

        self.btn_editar = Button(
            self.cuadro_cuatro,
            text='Editar', bg='darkorange', fg='white',
            font=('consolas',10,'bold'), padx=20, pady=5,
            command=self.editar_proveedor
        )
        self.btn_editar.pack(side=LEFT, padx=10)

        self.btn_guardar = Button(
            self.cuadro_cuatro,
            text='Guardar', bg='dodgerblue', fg='white',
            font=('consolas',10,'bold'), padx=20, pady=5,
            command=self.registrar_proveedor
        )
        self.btn_guardar.pack(side=LEFT, pady=10, padx=10)

        ### Tabla de proveedor
        self.tabla_proveedor = ttk.Treeview(
            self.cuadro_principal, height=10, columns=(0,1) 
        )

        self.tabla_proveedor.heading('#0', text='Nombre')
        self.tabla_proveedor.heading('#1', text='N° Celular')
        self.tabla_proveedor.heading('#2', text='Dirección')

        self.tabla_proveedor.pack(pady=10, padx=10)

        self.buscar_proveedor()

    def validacion(self):
        return len(self.entrada_nombre.get()) > 0 and\
            (len(self.entrada_celular.get()) > 0 and
             len(self.entrada_celular.get()) < 10) and\
            len(self.entrada_direccion.get())

    def buscar_proveedor(self):
        for elemento in self.tabla_proveedor.get_children():
            self.tabla_proveedor.delete(elemento)
        
        for fila in proveedor.obtener_proveedor():
            self.tabla_proveedor.insert('',0,text=fila[1],values=(fila[2], fila[3]), tags=fila[0])
    
    def registrar_proveedor(self):
        
        if self.validacion():
            proveedor = Proveedor(
                nombre=self.entrada_nombre.get(),
                celular=self.entrada_celular.get(),
                direccion=self.entrada_direccion.get()
                )
            proveedor.nuevo_proveedor(proveedor=proveedor)
            self.txt_mensaje.config(text='{0} registrado!'.format(proveedor.nombre), fg='springgreen')
            self.buscar_proveedor()

            self.entrada_nombre.delete(0, END)
            self.entrada_celular.delete(0, END)
            self.entrada_direccion.delete(0, END)
            self.entrada_nombre.focus()
        else:
            self.txt_mensaje.config(text='Datos Requeridos!', fg='crimson')
    
    def eliminar_proveedor(self):
        self.txt_mensaje.config(text='')
        try:
            id_proveedor = self.tabla_proveedor.item(self.tabla_proveedor.selection())['tags'][0]
            confirmar = messagebox.askretrycancel(title='Alerta', message='Estas seguro de eliminar?')

            if confirmar:
                proveedor.remover_proveedor(id_proveedor=id_proveedor)
                self.txt_mensaje.config(text='Proveedor eliminado', fg='crimson')
                self.buscar_proveedor()
            else:
                self.txt_mensaje.config(text='No eliminado', fg='limegreen')
                

        except IndexError:
            self.txt_mensaje.config(text='Seleciona un proveedor', fg='red')
    
    def editar_proveedor(self):
        self.txt_mensaje.config(text='')

        try:
            self.tabla_proveedor.item(self.tabla_proveedor.selection())['tags'][0]

            ### Ventana  editar
            self.formulario_editar = Toplevel()
            self.formulario_editar.geometry('350x300')
            self.formulario_editar.iconbitmap('img/logo.ico')

            nombre = self.tabla_proveedor.item(self.tabla_proveedor.selection())['text']
            celular = self.tabla_proveedor.item(self.tabla_proveedor.selection())['values'][0]
            direccion = self.tabla_proveedor.item(self.tabla_proveedor.selection())['values'][1]
            id_proveedor = self.tabla_proveedor.item(self.tabla_proveedor.selection())['tags'][0]

            self.datos_viejos = Label(
                self.formulario_editar, 
                text='nombre: {0}\n celular: {1}\n direccion: {2}'.format(nombre,celular,direccion),
                font=('cosolas',12,'bold'), pady=20, padx=10, fg='darkgoldenrod'
            )
            self.datos_viejos.pack(padx=20, pady=10)

            ### Entradas

            self.cuadro_1 = Label(self.formulario_editar)
            self.cuadro_1.pack()
            self.nombre_txt = Label(self.cuadro_1, text='Nombre: ')
            self.nombre_txt.pack(side=LEFT)
            self.nombre = Entry(self.cuadro_1)
            self.nombre.focus()
            self.nombre.pack(side=LEFT)
            
            self.cuadro_2 = Label(self.formulario_editar)
            self.cuadro_2.pack()
            self.celular_txt = Label(self.cuadro_2, text='Celular:    ')
            self.celular_txt.pack(side=LEFT)
            self.celular = Entry(self.cuadro_2)
            self.celular.pack(side=LEFT)

            self.cuadro_3 = Label(self.formulario_editar)
            self.cuadro_3.pack()
            self.direccion_txt = Label(self.cuadro_3, text='Direccion:')
            self.direccion_txt.pack(side=LEFT)
            self.direccion = Entry(self.cuadro_3)
            self.direccion.pack(side=LEFT)

            self.btn_edicion = Button(
                self.formulario_editar,
                text='Editar', fg='white', bg='chocolate',
                font=('consolas',12,'bold'), padx=20,
                command= lambda:self.actualizar(self.nombre.get(), self.celular.get(), self.direccion.get(), id_proveedor)
            ).pack(padx=10, pady=10)

        except IndexError:
            self.txt_mensaje.config(text='Seleciona un proveedor', fg='darkred')
        
    
    def actualizar(self, nombre,celular,direccion, id_proveedor):
        proveedor = Proveedor(nombre=nombre, celular=celular, direccion=direccion)
        proveedor.actualizar_proveedor(proveedor=proveedor, id_proveedor=id_proveedor)

        self.formulario_editar.destroy()
        self.txt_mensaje.config(text='Proveedor editado', fg='limegreen')

        self.buscar_proveedor()

