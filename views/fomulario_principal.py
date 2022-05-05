from tkinter import Label, GROOVE, Frame
from tkinter import ttk

### Formularios
from views.formulario_empleado import FormularioEmpleado
from views.formulario_paciente import FormularioPaciente
from views.formulario_historial import FormularioHistorial

class FormularioPrincipal:

    def __init__(self, ventana, id_empleado, tipo):
        self.ventana = ventana
        self.ventana.title('clínica'.title())
        self.ventana.geometry('1000x700+300+50')
        self.ventana.minsize(width=1000, height=700)
        self.ventana.iconbitmap('img/logo.ico')

        #Titulo
        self.titulo = Label(
            ventana,
            text='clínica de rehabilitación'.title(),
            fg='dodgerblue',
            font=('consolas', 18, 'bold'),
            relief=GROOVE,
            bd=3, padx=10, pady=10
        )
        self.titulo.pack(pady=10, padx=10)

        ### Menu de vistas
        self.vistas = ttk.Notebook(ventana)
        self.vistas.pack()

        

        ### Vista principal
        self.vista_principal = Frame(self.vistas, height=500, width=900)
        self.vistas.add(
            self.vista_principal,
            text='historial clínico'.title(),
        )
        FormularioHistorial(ventana=self.vista_principal)

        ### Vista empleado
        self.vista_empleado = Frame(self.vistas, height=500, width=900)
        self.vistas.add(
            self.vista_empleado,
            text='empleado'.title()
        )
        
        FormularioEmpleado(ventana=self.vista_empleado)

        if tipo == 'Administrador':
            pass
        else:
            self.vistas.hide(1)

        ### Vista paciente

        self.vista_paciente = Frame(self.vistas, height=500, width=900)
        self.vistas.add(
            self.vista_paciente,
            text='paciente'.title()
        )

        FormularioPaciente(ventana=self.vista_paciente, id_empleado=id_empleado)


       