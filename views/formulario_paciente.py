from tkinter import Label, LabelFrame, Entry, Button, LEFT ,END, CENTER, IntVar, Toplevel, StringVar
from tkinter import ttk
from tkinter.ttk import Treeview
from tkcalendar import Calendar
from datetime import date

### Entidades
from models.entidad_paciente import Paciente

paciente = Paciente(nombre='', apellido='', celular='',
                    genero='', dni='', peso=0, talla=0, fecha_nacimiento='')

class FormularioPaciente:

    def __init__(self,ventana, id_empleado):
        self.ventana = ventana
        self.codigo = id_empleado
        
        ### Cuadro Principal
        self.cuadro_principal = LabelFrame(
            self.ventana, text='Registrar Pacientes',
            fg='royalblue',
            font=('consolas',15,'bold'),
            padx=10,pady=10
        )
        self.cuadro_principal.pack()

        ### Cuadro Uno
        self.cuadro_uno = Label(self.cuadro_principal)
        self.cuadro_uno.pack(padx=10, pady=10)

        self.txt_nombre = Label(
            self.cuadro_uno, text='Nombre',
            font=('arial',10,'bold')
        )
        self.txt_nombre.pack(side=LEFT)

        self.entrada_nombre = Entry(
            self.cuadro_uno, font=('arial',10,'bold'),
            width=18, bd=3
        )
        self.entrada_nombre.pack(side=LEFT)

        self.txt_apellido = Label(
            self.cuadro_uno, text='Apellido',
            font=('arial',10,'bold')
        )
        self.txt_apellido.pack(side=LEFT)

        self.entrada_apellido = Entry(
            self.cuadro_uno, font=('arial',10,'bold'),
            width=18, bd=3
        )
        self.entrada_apellido.pack(side=LEFT)

        self.txt_celular = Label(
            self.cuadro_uno, text='Celular',
            font=('arial',10,'bold')
        )
        self.txt_celular.pack(side=LEFT)

        self.entrada_celular = Entry(
            self.cuadro_uno, font=('arial',10,'bold'),
            width=18, bd=3
        )
        self.entrada_celular.pack(side=LEFT)

        ### Cuadro Dos
        self.cuadro_dos = Label(self.cuadro_principal)
        self.cuadro_dos.pack(padx=10, pady=10)

        self.txt_genero = Label(
            self.cuadro_dos, text='Genero',
            font=('arial',10,'bold')
        )
        self.txt_genero.pack(side=LEFT)

        self.entrada_genero = ttk.Combobox(
            self.cuadro_dos, font=('arial',10,'bold'), state='readonly',
            width=10, values=('M','F'), justify=CENTER
        )
        self.entrada_genero.current(0)
        self.entrada_genero.pack(side=LEFT)

        self.txt_dni = Label(
            self.cuadro_dos, text='  DNI   ',
            font=('arial',10,'bold')
        )
        self.txt_dni.pack(side=LEFT)

        self.entrada_dni = Entry(
            self.cuadro_dos, font=('arial',10,'bold'),
            width=14, bd=3
        )
        self.entrada_dni.pack(side=LEFT)

        
        self.txt_peso = Label(
            self.cuadro_dos, text='  Peso ',
            font=('arial',10,'bold')
        )
        self.txt_peso.pack(side=LEFT)

        self.entrada_peso = Entry(
            self.cuadro_dos, font=('arial',10,'bold'),
            width=12, bd=3, justify=CENTER, 
            textvariable=IntVar(self.cuadro_dos, value=0)
        )
        self.entrada_peso.pack(side=LEFT)

        self.txt_talla = Label(
            self.cuadro_dos, text='Talla ',
            font=('arial',10,'bold')
        )
        self.txt_talla.pack(side=LEFT)

        self.entrada_talla = Entry(
            self.cuadro_dos, font=('arial',10,'bold'),
            width=12, bd=3, justify=CENTER,
            textvariable=IntVar(self.cuadro_dos, value=0)
        )
        self.entrada_talla.pack(side=LEFT)

        ### Cuadro Tres
        self.cuadro_tres = Label(self.cuadro_principal)
        self.cuadro_tres.pack(padx=10)

        self.txt_fecha = Label(
            self.cuadro_tres, text='Fecha Nacimiento',
            font=('arial',10,'bold')
        )
        self.txt_fecha.pack(side=LEFT)

        self.entrada_fecha = Calendar(
            self.cuadro_tres, selectmode='day', year=1999, 
            month=date.today().month, day=date.today().day
        )
        self.entrada_fecha.pack(side=LEFT)

        ### Mesajes
        self.txt_mensaje = Label(self.cuadro_principal, font=('consolas',12,'bold'))
        self.txt_mensaje.pack(padx=20, pady=10)

        ### Cuadro botones
        self.cuadro_botones = Label(self.cuadro_principal)
        self.cuadro_botones.pack(padx=10, pady=10)

        self.btn_editar = Button(
            self.cuadro_botones, 
            text='Editar', bg='darkorange', fg='white',
            font=('arila',10,'bold'), padx=20, pady=5,
            command=self.editar_paciente
        )
        self.btn_editar.pack(side=LEFT, padx=10)

        self.btn_guardar = Button(
            self.cuadro_botones, 
            text='Guardar', bg='dodgerblue', fg='white',
            font=('arila',10,'bold'), padx=20, pady=5,
            command=self.registrar_paciente
        )

        self.btn_guardar.pack(side=LEFT, padx=10)

        self.btn_buscar = Button(
            self.cuadro_botones,
            text='Buscar', bg='seagreen', fg='white',
            font=('arila', 10, 'bold'), padx=20, pady=5,
            command=self.leer_paciente
        )
        self.btn_buscar.pack(side=LEFT, padx=10)

        self.entrada_buscar_paciente = Entry(
            self.cuadro_principal, font=('consolas', 12, 'bold'),
            width=40, fg='green', bd=5
        )
        self.entrada_buscar_paciente.pack()

        ### Tabla de pacientes
        self.tabla_paciente = Treeview(
            self.cuadro_principal, height=10, columns=(0,1,2,3,4)
        )
        self.tabla_paciente.heading('#0', text='Nombre y Apellidos')
        self.tabla_paciente.heading('#1', text='Celular')
        self.tabla_paciente.heading('#2', text='DNI')
        self.tabla_paciente.heading('#3', text='Peso')
        self.tabla_paciente.heading('#4', text='Talla')
        self.tabla_paciente.heading('#5', text='Nacimiento')

        self.tabla_paciente.pack()

        self.buscar_paciente()
        
    
    def validar(self):
        return len(self.entrada_nombre.get()) > 0 and \
            len(self.entrada_apellido.get()) > 0 and \
            len(self.entrada_celular.get()) > 0 and len(self.entrada_celular.get()) < 10 and \
            len(self.entrada_dni.get()) > 0 and len(self.entrada_dni.get()) < 9 and \
            len(self.entrada_peso.get()) > 0 and \
            self.entrada_peso.get() != '0' and \
            len(self.entrada_talla.get()) > 0 and \
            self.entrada_peso.get() != '0'

    def buscar_paciente(self):
        ### limpiar datos
        for elemento in self.tabla_paciente.get_children():
            self.tabla_paciente.delete(elemento)

        ### llenar datos
        for fila in paciente.obtener_paciente():
            self.tabla_paciente.insert('', 0, text=fila[1]+', '+fila[2], values=(
                fila[3], fila[5], fila[6], fila[7], fila[8]), tags=fila[0])

    def leer_paciente(self):

        for e in self.tabla_paciente.get_children():
            self.tabla_paciente.delete(e)

        for fila in paciente.buscar_paciente(informacion=dict(ILIKE='%'+self.entrada_buscar_paciente.get()+'%')):
            self.tabla_paciente.insert('', 0, text=fila[1]+', '+fila[2], values=(
                fila[3], fila[5], fila[6], fila[7], fila[8]), tags=fila[0])

    def registrar_paciente(self):

        if self.validar():
            paciente = Paciente(nombre=self.entrada_nombre.get(), 
            apellido=self.entrada_apellido.get(), 
            celular=self.entrada_celular.get(),
            genero=self.entrada_genero.get(), dni=self.entrada_dni.get(), 
            peso=self.entrada_peso.get(), talla=self.entrada_talla.get(), 
            fecha_nacimiento=self.entrada_fecha.get_date())

            paciente.nuevo_paciente(paciente=paciente,id_empleado=self.codigo)
            self.buscar_paciente()
            
            self.txt_mensaje.config(text='{0} Registrado!'.format(paciente.nombre), fg='limegreen')

            self.entrada_nombre.focus()
            self.entrada_nombre.delete(0, END)
            self.entrada_apellido.delete(0, END)
            self.entrada_celular.delete(0, END)
            self.entrada_genero.current(0)
            self.entrada_dni.delete(0, END)
            self.entrada_peso.config(textvariable=IntVar(self.cuadro_dos, value=0))
            self.entrada_talla.config(textvariable=IntVar(self.cuadro_dos, value=0))

        else:
            self.txt_mensaje.config(text='Faltan datos', fg='crimson')
    
    def editar_paciente(self):
        try:
            id_paciente = self.tabla_paciente.item(self.tabla_paciente.selection())['tags'][0]
            nombre = self.tabla_paciente.item(self.tabla_paciente.selection())['text']
            celular = self.tabla_paciente.item(self.tabla_paciente.selection())['values'][0]
            dni = self.tabla_paciente.item(self.tabla_paciente.selection())['values'][1]
            peso = self.tabla_paciente.item(self.tabla_paciente.selection())['values'][2]
            talla = self.tabla_paciente.item(self.tabla_paciente.selection())['values'][3]
            fecha = self.tabla_paciente.item(self.tabla_paciente.selection())['values'][4]
    
            nombre_n = nombre.split(',')

            self.formulario_editar = Toplevel()
            self.formulario_editar.title('Editar Paciente')
            self.formulario_editar.geometry('600x200')
            self.formulario_editar.iconbitmap('img/logo.ico')

            ### Entradas
            self.cuadro_1 = Label(self.formulario_editar)
            self.cuadro_1.pack()
            
            self.cuadro_2 = Label(self.formulario_editar)
            self.cuadro_2.pack()

            self.cuadro_3 = Label(self.formulario_editar)
            self.cuadro_3.pack()

            self.cuadro_4 = Label(self.formulario_editar)
            self.cuadro_4.pack()

            self.cuadro_5 = Label(self.formulario_editar)
            self.cuadro_5.pack()

            self.nombre_txt = Label(self.cuadro_1, text='Nombre', font=('arial',10,'bold'))
            self.nombre_txt.pack(side=LEFT)

            self.nuevo_nombre = Entry(
                self.cuadro_1, font=('arial',10,'bold'),
                textvariable=StringVar(self.cuadro_1, value=nombre_n[0])
            )
            self.nuevo_nombre.pack(side=LEFT)

            self.apellido_txt = Label(self.cuadro_1, text='Apellido', font=('arial',10,'bold'))
            self.apellido_txt.pack(side=LEFT)

            self.nuevo_apellido = Entry(
                self.cuadro_1, font=('arial',10,'bold'),
                textvariable=StringVar(self.cuadro_1, value=nombre_n[1])
            )
            self.nuevo_apellido.pack(side=LEFT)

            self.celular_txt = Label(self.cuadro_2, text='Celular', font=('arial',10,'bold'))
            self.celular_txt.pack(side=LEFT)

            self.nuevo_celular = Entry(
                self.cuadro_2, font=('arial',10,'bold'),
                textvariable=StringVar(self.cuadro_2, value=celular)
            )
            self.nuevo_celular.pack(side=LEFT)

       
            self.genero_txt = Label(self.cuadro_2, text='Genero', font=('arial',10,'bold'))
            self.genero_txt.pack(side=LEFT)
            self.nuevo_genero = ttk.Combobox(
                self.cuadro_2, font=('arial',10,'bold'), width=14,
                values=('M','F'), justify=CENTER, state='readonly'
            )
            self.nuevo_genero.current(0)
            self.nuevo_genero.pack(side=LEFT)


            self.dni_txt = Label(self.cuadro_3, text='DNI', font=('arial',10,'bold'))
            self.dni_txt.pack(side=LEFT)
            self.nuevo_dni = Entry(
                self.cuadro_3, font=('arial',10,'bold'), width=14,
                textvariable=StringVar(self.cuadro_2, value=dni)
            )
            self.nuevo_dni.pack(side=LEFT)

            self.peso_txt = Label(self.cuadro_3, text='Peso', font=('arial',10,'bold'))
            self.peso_txt.pack(side=LEFT)
            self.nuevo_peso = Entry(
                self.cuadro_3, font=('arial',10,'bold'), width=12,
                textvariable=StringVar(self.cuadro_3, value=peso)
            )
            self.nuevo_peso.pack(side=LEFT)

            self.talla_txt = Label(self.cuadro_4, text='Talla', font=('arial',10,'bold'))
            self.talla_txt.pack(side=LEFT)
            self.nuevo_talla = Entry(
                self.cuadro_4, font=('arial',10,'bold'), width=12,
                textvariable=StringVar(self.cuadro_4, value=talla)
            )
            self.nuevo_talla.pack(side=LEFT)


            self.fecha_txt = Label(self.cuadro_4, text='Fecha', font=('arial',10,'bold'))
            self.fecha_txt.pack(side=LEFT)
            self.nuevo_fecha = Entry(
                self.cuadro_4, font=('arial',10,'bold'), width=12,
                textvariable=StringVar(self.cuadro_4, value=fecha)
            )
            self.nuevo_fecha.pack(side=LEFT)
     

            ### Boton Actualizar
            self.btn_actualizar = Button(
                self.formulario_editar, text='Actualizar',
                font=('arial', 13, 'bold'), fg='white', bg='chocolate',
                command= lambda: self.actualizar(
                    self.nuevo_nombre.get(),
                    self.nuevo_apellido.get(),
                    self.nuevo_celular.get(),
                    self.nuevo_genero.get(),
                    self.nuevo_dni.get(),
                    self.nuevo_peso.get(),
                    self.nuevo_talla.get(),
                    self.nuevo_fecha.get(),
                    id_paciente
                )
            ).pack()

        except IndexError:
            self.txt_mensaje.config(text='Selecciona un Dato', fg='crimson')
    
    def actualizar(self, nombre, apellido, celular, genero, dni, peso, talla, fecha, id_paciente):
        paciente = Paciente(nombre=nombre, apellido=apellido, celular=celular,
                            genero=genero, dni=dni, peso=peso, talla=talla, fecha_nacimiento=fecha)

        paciente.actualizar_paciente(
            paciente=paciente, id_paciente=id_paciente, id_empleado=self.codigo)

        self.formulario_editar.destroy()
        self.txt_mensaje.config(text='Paciente {} Actualizado...'.format(paciente.nombre), fg='limegreen')

        self.buscar_paciente()
