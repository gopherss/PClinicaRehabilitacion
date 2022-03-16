from os import environ
from tkinter import *
from tkinter import messagebox
from cryptocode import decrypt

### Entidades
from models.entidad_empleado import Empleado

### Formularios
from views.fomulario_principal import FormularioPrincipal

empleado = Empleado(nombre='',apellido='',tipo='',celular='',dni='',estado=True,contrasenia='')

class Login:

    def __init__(self, ventana):
        self.ventana = ventana

        self.ventana.title('Sesión')
        self.ventana.geometry('300x400+600+100')
        self.ventana.iconbitmap('img/logo.ico')
        self.ventana.maxsize(width=300, height=400)
        self.ventana.minsize(width=300, height=400)
        self.ventana.config(bg='#263238')

        ### Imagen
        self.user = PhotoImage(file='img/user.png')

        self.txt_imagen = Label(
            self.ventana,
            image=self.user, 
            width=100, height=100
        )
        self.txt_imagen.pack(pady=20)

        ### Cuadro uno
        self.cuadro_uno = Label(self.ventana, bg='#263238')
        self.cuadro_uno.pack(padx=10, pady=10)

        self.txt_nombre = Label(
            self.cuadro_uno, text='  Nombre  ',
            bg='#263238', fg='white',
            font=('consolas',15,'bold')
        )
        self.txt_nombre.pack(side=LEFT)

        self.entrada_nombre = Entry(
            self.cuadro_uno, relief=GROOVE, bd=2,
            font=('consolas',15,'bold'), width=12
        )
        self.entrada_nombre.focus()
        self.entrada_nombre.pack(side=LEFT)

        ### Cuadro dos
        self.cuadro_dos = Label(self.ventana, bg='#263238')
        self.cuadro_dos.pack(padx=10, pady=10)

        self.txt_contrasenia = Label(
            self.cuadro_dos, text='Contraseña',
            bg='#263238', fg='white',
            font=('consolas',15,'bold')
        )
        self.txt_contrasenia.pack(side=LEFT)

        self.entrada_contrasenia = Entry(
            self.cuadro_dos, show='*', relief=GROOVE, bd=2,
            font=('consolas',15,'bold'), width=12
        )
        self.entrada_contrasenia.pack(side=LEFT)

        ### Mensajes
        self.txt_mensaje = Label(
            self.ventana,font=('consolas',15,'bold'),
            bg='#263238', fg='lavender'
        )
        self.txt_mensaje.pack(pady=10)

        ### Cuadro tres
        self.cuadro_tres = Label(self.ventana, bg='#263238')
        self.cuadro_tres.pack(padx=10, pady=10)

        self.btn_ingresar = Button(
            self.cuadro_tres, text='Ingresar',
            fg='white', bg='dodgerblue',
            padx=20, pady=5, font=('consolas',11,'bold'),
            command=self.loguear
        )

        self.btn_ingresar.pack(side=RIGHT, padx=10)

        self.btn_limpiar = Button(
            self.cuadro_tres, text=' Limpiar ',
            fg='white', bg='goldenrod',
            padx=20, pady=5, font=('consolas',11,'bold'),
            command=self.borrar_entradas
        )
        self.btn_limpiar.pack(side=LEFT, padx=10)

    def borrar_entradas(self):
        self.entrada_nombre.delete(0, END)
        self.entrada_contrasenia.delete(0, END)
        self.entrada_nombre.focus()
        self.txt_mensaje.config(text='')
    
    def validar_datos(self):
        return len(self.entrada_nombre.get()) > 0 and\
            len(self.entrada_contrasenia.get()) > 0

    def loguear(self):
        if self.validar_datos():
            nombre = self.entrada_nombre.get()
            password = self.entrada_contrasenia.get()

            estado = bool() 
            codigo = str()
            

            for empleados in empleado.obtener_empleado():

                if nombre == empleados[1] and password == decrypt(empleados[7],environ.get('pgsecret')) and empleados[6] == True:
                    estado = True
                    codigo = empleados[0]
                    break
                else:
                    estado = False
                    continue
            
            if estado:     
                messagebox.showinfo(title='Felicidades', message='Acceso consedido')
                self.ventana.destroy()

                vista = Tk()
                FormularioPrincipal(ventana=vista, id_empleado=codigo)
                vista.mainloop()
            else:
                self.txt_mensaje.config(text='Acceso denegado')

        else:
            self.txt_mensaje.config(text='Faltan datos', fg='red')

