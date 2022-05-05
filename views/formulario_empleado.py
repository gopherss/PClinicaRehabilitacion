from tkinter import Label, LabelFrame, Entry, Button, END, LEFT, CENTER, StringVar, Toplevel
from tkinter import ttk
from models.entidad_empleado import Empleado
from cryptocode import encrypt, decrypt
from os import environ


empleado = Empleado(nombre='', apellido='', tipo='', celular='',dni='',estado=True, contrasenia='')

class FormularioEmpleado:

    def __init__(self, ventana):
        self.ventana = ventana
        self.cuadro_principal = LabelFrame(
            self.ventana,
            text='registrar empleado'.title(),
            font=('consolas', 15, 'bold'),
            fg='royalblue'
        )
        self.cuadro_principal.pack()

        ### cuadro uno
        self.cuadro_uno = Label(self.cuadro_principal)
        self.cuadro_uno.pack(pady=10, padx=10)

        self.txt_nombre = Label(
            self.cuadro_uno,
            text='Nombre: ',
            font=('arial',10,'bold')
        )
        self.txt_nombre.pack(side=LEFT)

        self.entrada_nombre = Entry(
            self.cuadro_uno, width=25, bd=3,
            font=('arial',10,'bold')
        )
        self.entrada_nombre.pack(side=LEFT)

        self.txt_apellido = Label(
            self.cuadro_uno,
            text='Apellido: ',
            font=('arial',10,'bold')
        )
        self.txt_apellido.pack(side=LEFT)

        self.entrada_apellido = Entry(
            self.cuadro_uno, width=25, bd=3,
            font=('arial',10,'bold')
        )
        self.entrada_apellido.pack(side=LEFT)

        ### Cuadro dos
        self.cuadro_dos = Label(self.cuadro_principal)
        self.cuadro_dos.pack(pady=10, padx=10)

        self.txt_celular = Label(
            self.cuadro_dos,
            text='Celular:',
            font=('arial',10,'bold')
        )
        self.txt_celular.pack(side=LEFT)

        self.entrada_celular = Entry(
            self.cuadro_dos, bd=3, justify=CENTER ,
            font=('arial',10,'bold'), width=25,
        )
        self.entrada_celular.pack(side=LEFT)

        self.txt_tipo = Label(
            self.cuadro_dos,
            text='Tipo:     ',
            font=('arial',10,'bold')
        )
        self.txt_tipo.pack(side=LEFT)

        self.combo_tipo = ttk.Combobox(
            self.cuadro_dos, state='readonly',
            values=('Administrador','Empleado'),
            font=('arial',10,'bold'), width=23,
        )
        self.combo_tipo.current(0)
        self.combo_tipo.pack(side=LEFT)

        ### Cuadro tres
        self.cuadro_tres = Label(self.cuadro_principal)
        self.cuadro_tres.pack(pady=10, padx=10)
        
        self.txt_dni = Label(
            self.cuadro_tres,
            text='DNI:    ',
            font=('arial',10,'bold')
        )
        self.txt_dni.pack(side=LEFT)

        self.entrada_dni = Entry(
            self.cuadro_tres, width=25 , bd=3,
            font=('arial',10,'bold')
        )
        self.entrada_dni.pack(side=LEFT)

        self.txt_estado = Label(
            self.cuadro_tres,
            text='Estado:   ',
            font=('arial',10,'bold')
        )
        self.txt_estado.pack(side=LEFT)

        self.combo_estado = ttk.Combobox(
            self.cuadro_tres,state='readonly',
            values=('Activo', 'Inactivo'),
            font=('arial',10,'bold'), width=22
        )
        self.combo_estado.current(0)
        self.combo_estado.pack(side=LEFT)

        ### Cuadro cuatro
        self.cuadro_cuatro = Label(self.cuadro_principal)
        self.cuadro_cuatro.pack(padx=10, pady=10)

        self.txt_contrasenia = Label(
            self.cuadro_cuatro,
            text='Contraseña',
            font=('arial',10,'bold')
        )
        self.txt_contrasenia.pack(side=LEFT)

        self.entrada_contrasenia = Entry(
            self.cuadro_cuatro, width=20,
            show='■', fg='royalblue',
            font=('arial',11,'bold')
        )
        self.entrada_contrasenia.pack(side=LEFT)
        
        ### texto Mensajes
        self.txt_mensaje = Label(
            self.cuadro_principal,
            font=('consolas',13,'bold')
        )
        self.txt_mensaje.pack(padx=20, pady=10)


        ### cuadro cinco
        self.cuadro_cinco = Label(self.cuadro_principal)
        self.cuadro_cinco.pack(pady=10, padx=10)


        self.btn_editar = Button(
            self.cuadro_cinco,
            text='Editar', bg='darkorange', fg='white',
            font=('consolas', 10, 'bold'), padx=20, pady=5,
            command=self.editar_empleado
        )
        self.btn_editar.pack(side=LEFT, padx=10)

        self.btn_guardar = Button(
            self.cuadro_cinco,
            text='Guardar',  bg='dodgerblue', fg='white',
            font=('consolas', 10, 'bold'), padx=20, pady=5,
            command=self.registrar_empleado
        )
        self.btn_guardar.pack(side=LEFT, padx=10)

        self.btn_buscar = Button(
            self.cuadro_cinco,
            text='Buscar',  bg='#43a047', fg='white',
            font=('consolas', 10, 'bold'), padx=20, pady=5,
            command=self.leer_empleado
        )
        self.btn_buscar.pack(side=LEFT)
        ### cuadro de busqueda
        self.entrada_buscar_empleado = Entry(
            self.cuadro_principal, font=('consolas', 12, 'bold'),
            width=40, fg='green', bd=5
        )
        self.entrada_buscar_empleado.pack()

        ### tabla empleado
        self.tabla_empleado = ttk.Treeview(
            self.cuadro_principal,height=10, columns=(0,1,2,3)
        )

        self.tabla_empleado.heading('#0', text='Nombre')
        self.tabla_empleado.heading('#1', text='Apellido')
        self.tabla_empleado.heading('#2', text='Tipo')
        self.tabla_empleado.heading('#3', text='DNI')
        self.tabla_empleado.heading('#4', text='Estado')

        self.tabla_empleado.pack(padx=10, pady=10)
        self.buscar_empleado()

    def validacion(self):
        return len(self.entrada_nombre.get()) > 0 and \
            len(self.entrada_apellido.get()) > 0 and \
            (len(self.entrada_celular.get()) > 0 and len(self.entrada_celular.get()) < 10) and \
            (len(self.entrada_dni.get()) > 0 and len(self.entrada_dni.get()) < 9) and \
            len(self.entrada_contrasenia.get()) > 0

    
    def buscar_empleado(self):

        for elemento in self.tabla_empleado.get_children():
            self.tabla_empleado.delete(elemento)
        ## validamos si la fila es verdadero o falso segun sea activo por el usuario
        for fila in empleado.obtener_empleado():
            if fila[6]:
                self.tabla_empleado.insert('',0,text=fila[1], values=(fila[2],fila[3],fila[5],'Activo',fila[7], fila[4]), tags=fila[0])
            else:
                self.tabla_empleado.insert('',0,text=fila[1], values=(fila[2],fila[3],fila[5],'Inactivo',fila[7], fila[4]), tags=fila[0])
    
    def leer_empleado(self):
        for elemento in self.tabla_empleado.get_children():
            self.tabla_empleado.delete(elemento)
        
        for fila in empleado.leer_empleado(informacion=dict(ILIKE = '%'+self.entrada_buscar_empleado.get()+'%')):
            if fila[6]:
                self.tabla_empleado.insert('',0,text=fila[1], values=(fila[2],fila[3],fila[5],'Activo',fila[7], fila[4]), tags=fila[0])
            else:
                self.tabla_empleado.insert('',0,text=fila[1], values=(fila[2],fila[3],fila[5],'Inactivo',fila[7], fila[4]), tags=fila[0])


    def registrar_empleado(self):
        if self.validacion():
            estado = bool
            if self.combo_estado.get() == 'Activo':
                estado = True
            else:
                estado = False
            empleado = Empleado(
                nombre=self.entrada_nombre.get().lower(),
                apellido=self.entrada_apellido.get(),
                tipo=self.combo_tipo.get(),
                celular=self.entrada_celular.get(),
                dni=self.entrada_dni.get(),
                estado=estado,
                contrasenia= encrypt(self.entrada_contrasenia.get(), environ.get('pgsecret'))
            )

            empleado.nuevo_empleado(empleado=empleado)
            self.txt_mensaje.config(text='{0}: Registrado! '.format(empleado.nombre), fg='limegreen')
            self.buscar_empleado()

            self.entrada_nombre.delete(0, END)
            self.entrada_apellido.delete(0, END)
            self.combo_tipo.current(0)
            self.entrada_celular.delete(0, END)
            self.entrada_dni.delete(0, END)
            self.combo_estado.current(0)
            self.entrada_contrasenia.delete(0, END)
            self.entrada_nombre.focus()
        else:
            self.txt_mensaje.config(text='Se requieren Datos', fg='crimson')
    

    
    def editar_empleado(self):
        
        try:
            id_empleado = self.tabla_empleado.item(self.tabla_empleado.selection())['tags'][0]
            nombre = self.tabla_empleado.item(self.tabla_empleado.selection())['text']
            apellido = self.tabla_empleado.item(self.tabla_empleado.selection())['values'][0]
            celular = self.tabla_empleado.item(self.tabla_empleado.selection())['values'][5]
            dni = self.tabla_empleado.item(self.tabla_empleado.selection())['values'][2]
            contrasenia = self.tabla_empleado.item(self.tabla_empleado.selection())['values'][4]

            ### Contraseña desencriptada
            contrasenia_txt = decrypt(contrasenia, environ.get('pgsecret'))


            self.formulario_editar = Toplevel()
            self.formulario_editar.iconbitmap('img/logo.ico')
            self.formulario_editar.geometry('500x200')

            self.cuadro_1 = Label(self.formulario_editar)
            self.cuadro_1.pack()
            self.cuadro_2 = Label(self.formulario_editar)
            self.cuadro_2.pack()
            self.cuadro_3 = Label(self.formulario_editar)
            self.cuadro_3.pack()
            self.cuadro_5 = Label(self.formulario_editar)
            self.cuadro_5.pack()
            

            self.nombre_txt = Label(self.cuadro_1, text='Nombre: ')
            self.nombre_txt.pack(side=LEFT)
            self.nombre = Entry(self.cuadro_1, textvariable=StringVar(self.cuadro_1, value=nombre))
            self.nombre.pack(side=LEFT)
            self.nombre.focus()

            self.apellido_txt = Label(self.cuadro_1, text='Apellido: ')
            self.apellido_txt.pack(side=LEFT)
            self.apellido = Entry(self.cuadro_1, textvariable=StringVar(self.cuadro_1, value=apellido))
            self.apellido.pack(side=LEFT)

            self.celular_txt = Label(self.cuadro_2, text='Celular: ')
            self.celular_txt.pack(side=LEFT)
            self.celular = Entry(self.cuadro_2, textvariable=StringVar(self.cuadro_2, value=celular))
            self.celular.pack(side=LEFT)

            self.tipo_txt = Label(self.cuadro_2, text='Tipo: ')
            self.tipo_txt.pack(side=LEFT)
            if nombre.lower() == 'jeiner':
                self.tipo = ttk.Combobox(self.cuadro_2, values=('Administrador','Empleado'), state='disable')
            else:
                self.tipo = ttk.Combobox(self.cuadro_2, values=('Administrador','Empleado'), state='readonly')
            self.tipo.current(0)
            self.tipo.pack(side=LEFT)

            self.dni_txt = Label(self.cuadro_3, text='DNI: ')
            self.dni_txt.pack(side=LEFT)
            self.dni = Entry(self.cuadro_3, textvariable=StringVar(self.cuadro_3, value=dni))
            self.dni.pack(side=LEFT)

            self.estado_txt = Label(self.cuadro_3, text='Estado: ')
            self.estado_txt.pack(side=LEFT)
            if nombre.lower() == 'jeiner':
                self.estado = ttk.Combobox(self.cuadro_3, values=('Activo', 'Inactivo'), state='disable')
            else:
                self.estado = ttk.Combobox(self.cuadro_3, values=('Activo', 'Inactivo'), state='readonly')
            self.estado.current(0)
            self.estado.pack(side=LEFT)

            self.contrasenia_txt = Label(self.cuadro_5, text='Contraseña')
            self.contrasenia_txt.pack(side=LEFT)

            self.contrasenia = Entry(self.cuadro_5, show='■', textvariable=StringVar(self.cuadro_5, contrasenia_txt))
            self.contrasenia.pack(side=LEFT)

            ## Boton Editar
            self.btn_edicion = Button(
                self.formulario_editar,
                text='Editar', font=('consolas',12,'bold'),
                fg='white',bg='chocolate',
                command= lambda : self.actualizar(self.nombre.get(),self.apellido.get(),self.tipo.get(),self.celular.get(),self.dni.get(),self.estado.get(),self.contrasenia.get(),id_empleado)
            )
            self.btn_edicion.pack(padx=20, pady=5)

        except IndexError:
            self.txt_mensaje.config(text='Selecciona un empleado', fg='brown')
    
    def actualizar(self,nombre,apellido,tipo,celular,dni,estado,contrasenia,id_empleado):
        nuevo_estado = bool

        if estado == 'Activo':
            nuevo_estado = True
        else:
            nuevo_estado = False

        empleado =  Empleado(nombre=nombre, 
        apellido=apellido, tipo=tipo, celular=celular,
        dni=dni,estado=nuevo_estado, 
        contrasenia=encrypt(contrasenia,environ.get('pgsecret'))
        )

        empleado.actualizar_empleado(empleado=empleado, id_empleado=id_empleado)
        
        self.formulario_editar.destroy()
        self.txt_mensaje.config(text='Empleado {0} editado con éxito'.format(empleado.nombre), fg='royalblue')
        self.buscar_empleado()
        
