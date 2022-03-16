from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Treeview
from matplotlib import image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from os import getlogin, mkdir

### Entidad
from models.entidad_paciente import Paciente
from models.entidad_diagnostico import Diagnostico

paciente = Paciente(nombre='', apellido='', celular='',
                    genero='', dni='', peso=0, talla=0, fecha_nacimiento='')
diagnostico = Diagnostico(diagnostico='', tratamiento='')

class FormularioHistorial:

    def __init__(self, ventana):
        self.ventana = ventana

        self.cuadro_principal = LabelFrame(
            self.ventana, text='Nuevo Historial Clinico',
            font=('consolas', 15, 'bold'),
            fg='royalblue', padx=10, pady=10
        )
        self.cuadro_principal.pack()

        ### Cuadro Uno
        self.cuadro_uno = Label(self.cuadro_principal)
        self.cuadro_uno.pack()

        self.tabla_pacientes = Treeview(
            self.cuadro_uno, height=5, columns=(0,)
        )
        self.tabla_pacientes.heading('#0', text='Paciente')
        self.tabla_pacientes.heading('#1', text='DNI')
        self.tabla_pacientes.pack(side=LEFT, padx=10)

        self.entrada_buscar_paciente = Entry(
            self.cuadro_uno, font=('consolas', 14, 'bold'),
            width=20, bd=3
        )
        self.entrada_buscar_paciente.pack(side=LEFT)

        self.btn_buscar_paciente = Button(
            self.cuadro_uno, font=('consolas', 12, 'bold'),
            width=10, bd=3, text='Buscar', bg='deepskyblue', fg='white'
        )
        self.btn_buscar_paciente.pack(side=LEFT)

        ### Cuadro Dos
        self.cuadro_dos = Label(self.cuadro_principal)
        self.cuadro_dos.pack()

        self.txt_diagnostico = Label(
            self.cuadro_dos, font=('arial', 10, 'bold'),
            text='Diagnostico'
        )
        self.txt_diagnostico.pack(side=LEFT)

        self.entrada_diagnostico = ScrolledText(
            self.cuadro_dos, width=25, height=5, bd=3,
            fg='royalblue', relief=GROOVE, font=('arial', 13, 'bold')
        )
        self.entrada_diagnostico.pack(side=LEFT, pady=10)

        self.txt_tratamiento = Label(
            self.cuadro_dos, font=('arial', 10, 'bold'),
            text='Indicaciones'
        )
        self.txt_tratamiento.pack(side=LEFT)

        self.entrada_tratamiento = ScrolledText(
            self.cuadro_dos, width=25, height=5, bd=3,
            fg='royalblue', relief=GROOVE, font=('arial', 13, 'bold')
        )
        self.entrada_tratamiento.pack(side=LEFT, pady=10)

        ### Cuadro botones
        self.cuadro_botones = Label(self.cuadro_principal)
        self.cuadro_botones.pack()

        self.btn_editar = Button(
            self.cuadro_botones, text='Editar', font=('arial', 10, 'bold'),
            fg='white', bg='darkorange', padx=20, pady=5,
            command=self.editar_diagnostico
        )
        self.btn_editar.pack(side=LEFT, padx=10)

        self.btn_guardar = Button(
            self.cuadro_botones, text='Guardar', font=('arial', 10, 'bold'),
            fg='white', bg='dodgerblue', padx=20, pady=5,
            command=self.registrar_diagnostico
        )
        self.btn_guardar.pack(side=LEFT, padx=10)

        self.btn_buscar = Button(
            self.cuadro_botones,
            text='Buscar', bg='seagreen', fg='white',
            font=('arila', 10, 'bold'), padx=20, pady=5
        )
        self.btn_buscar.pack(side=LEFT, padx=10)

        self.btn_imprimir = Button(
            self.cuadro_botones, 
            text='Imprimir', bg='brown', fg='white',
            font=('arial', 10, 'bold'), padx=20, pady=5,
            command=self.imprimir_pdf
        )
        self.btn_imprimir.pack(side=LEFT, padx=10)

        self.txt_mensaje = Label(
            self.cuadro_principal, font=('arial', 12, 'bold')
        )
        self.txt_mensaje.pack(pady=10)

        self.tabla_historial = Treeview(
            self.cuadro_principal, height=5, columns=(0, 1, 2)
        )
        self.tabla_historial.heading('#0', text='Paciente')
        self.tabla_historial.heading('#1', text='Genero')
        self.tabla_historial.heading('#2', text='Peso')
        self.tabla_historial.heading('#3', text='Talla')

        self.tabla_historial.pack()

        self.mostrar_paciente()
        self.mostrar_historial()

    def mostrar_paciente(self):
        for elemento in self.tabla_pacientes.get_children():
            self.tabla_pacientes.delete(elemento)

        for fila in paciente.obtener_paciente():
            self.tabla_pacientes.insert(
                '', 0, text=fila[1]+','+fila[2], values=(fila[5], fila[0]))
    
    def mostrar_historial(self):
        for elemento in self.tabla_historial.get_children():
            self.tabla_historial.delete(elemento)

        for fila in diagnostico.obtener_historial():
            self.tabla_historial.insert(
                '', 0, text=fila[0]+' '+fila[1], 
                values=(fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[9], fila[10]), 
                tags=fila[8])

    def validar(self):
        return len(self.entrada_diagnostico.get(1.0, END)) > 1 and \
            len(self.entrada_tratamiento.get(1.0, END)) > 1

    def registrar_diagnostico(self):
        try:
            if self.validar():
                texto_diagnostico = self.entrada_diagnostico.get(1.0, END)
                texto_tratamiento = self.entrada_tratamiento.get(1.0, END)
                codigo = self.tabla_pacientes.item(
                    self.tabla_pacientes.selection())['values'][1]

                mi_objeto = Diagnostico(diagnostico=texto_diagnostico.capitalize(),
                                        tratamiento=texto_tratamiento.capitalize())

                mi_objeto.nuevo_diagnostico(
                    mi_objeto=mi_objeto, id_paciente=codigo)

                self.txt_mensaje.config(text='Datos Guardados', fg='#1e88e5')
                self.mostrar_historial()

                self.entrada_diagnostico.delete(0.0, END)
                self.entrada_tratamiento.delete(0.0, END)
                self.entrada_diagnostico.focus()
                self.mostrar_paciente()
            else:
                self.txt_mensaje.config(text='Faltan Datos', fg='darkred')
        except IndexError:
            self.txt_mensaje.config(
                text='Selecciona un paciente', fg='chocolate')
    
    def editar_diagnostico(self):
        self.txt_mensaje.config(text='')
        try:
            self.tabla_historial.item(
                self.tabla_historial.selection()
            )['tags'][0]

            contenido_diagnostico = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['values'][3]
            contenido_tratamiento = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['values'][4]

            id_diagnostico = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['values'][6]

            id_tratamiento = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['values'][7]

            self.formulario_editar = Toplevel()
            self.formulario_editar.title('Nuevo Diagnostico')
            self.formulario_editar.geometry('500x400')
            self.formulario_editar.iconbitmap('img/logo.ico')

            ### Cuadro uno

            self.cuadro_1 = Label(self.formulario_editar)
            self.cuadro_1.pack()

            ### Entradas Diagnostico
            self.diagnostico_txt = Label(
                self.cuadro_1, text='Diagnostico'
            )
            self.diagnostico_txt.pack(side=LEFT)
            self.diagnostico = ScrolledText(
                self.cuadro_1, width=30, height=5, bd=3, 
                fg='royalblue', relief=GROOVE, font=('arial', 11, 'bold'),
            )
            self.diagnostico.pack(side=LEFT, pady=10)

            self.diagnostico.insert(0.0, contenido_diagnostico)

            ### Cuadro 2
            self.cuadro_2 = Label(self.formulario_editar)
            self.cuadro_2.pack()

            ### Entradas tratamiento
            self.tratamiento_txt = Label(
                self.cuadro_2, text='Tratamiento'
            )
            self.tratamiento_txt.pack(side=LEFT)
            self.tratamiento = ScrolledText(
                self.cuadro_2, width=30, height=5, bd=3, 
                fg='royalblue', relief=GROOVE, font=('arial', 11, 'bold'),
            )
            self.tratamiento.pack(side=LEFT, pady=10)
            self.tratamiento.insert(0.0, contenido_tratamiento)

            ## Boton actualizar
            self.btn_actualizar = Button(
                self.formulario_editar, text='Actualizar', fg='white', bg='chocolate',
                font=('consolas',13,'bold'), padx=15, pady=5,
                command= lambda: self.actualizar(self.diagnostico.get(0.0, END),
                 self.tratamiento.get(0.0, END), id_diagnostico, id_tratamiento)
            )
            self.btn_actualizar.pack()
            
        except IndexError:
            self.txt_mensaje.config(text='Selecione documento', fg='darkred')

    def actualizar(self, contenido_diagnostico, contenito_tratamiento, id_diagnostico, id_tratamiento):
        
        objeto = Diagnostico(diagnostico=contenido_diagnostico.capitalize(),
                             tratamiento=contenito_tratamiento.capitalize())

        objeto.actualizar_diagnostico(mi_objeto=objeto,
                                      id_diagnostico=id_diagnostico,
                                      id_tratamiento=id_tratamiento)
        
        self.formulario_editar.destroy()
        self.txt_mensaje.config(text='Historial editado correctamente', fg='limegreen')
        self.mostrar_historial()

    def imprimir_pdf(self):
        self.txt_mensaje.config(text='')
        try:
            self.tabla_historial.item(
                    self.tabla_historial.selection()
                )['tags'][0]

            nombre_completo = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['text']

            datos = self.tabla_historial.item(
                self.tabla_historial.selection()
            )['values']
            
            imc = paciente.calcular_imc(peso=float(datos[1]), talla=float(datos[2]))

            paciente_info = dict({
                'Nombre': nombre_completo,
                'Genero': datos[0],
                'Peso': datos[1],
                'Talla': datos[2],
                'IMC': imc 
            })

            #### Estructura del pdf
            w, h = A4

            try:
                mkdir('C:/Users/{0}/Escritorio/rep'.format(getlogin()))
            except OSError:
                pass

            ruta_pdf = 'C:/Users/{0}/Escritorio/rep/{1}_reporte.pdf'.format(getlogin(),nombre_completo)
            ruta_logo = 'img/logopdf.png'
            ruta_imc = 'img/imc.jpg'

            titulo = 'Clinica de Rehabilitación'

            diagnostico_texto = '''
            Diagnostico:\n{0}
            '''.format(datos[3])

            tratamiento_texto = '''
            Tratamiento:\n{0}
            '''.format(datos[4])

            reporte = Canvas(filename=ruta_pdf, pagesize=A4)

            reporte.drawImage(image=ruta_logo, x=20, y=h-80, width=61, height=61)

            titulo_clinica = reporte.beginText(150, h-90)
            titulo_clinica.setFont('Courier', 18)
            titulo_clinica.textLine(titulo)
            reporte.drawText(titulo_clinica)

            diagnostico = reporte.beginText(50, h-110)
            diagnostico.setFont('Times-Roman', 12)
            diagnostico.textLines(diagnostico_texto)
            reporte.drawText(diagnostico)

            tratamiento = reporte.beginText(50, h-220)
            tratamiento.setFont('Times-Roman', 12)
            tratamiento.textLines(tratamiento_texto)
            reporte.drawText(tratamiento)

            reporte.line(x1=50, y1=h-320, x2=500, y2=h-320)

            informacion_paciente = reporte.beginText(50, h-350)
            info_paciente = str('')

            for clave, valor in paciente_info.items():
                info_paciente += '{}:  {}\n'.format(str(clave),str(valor))
            
            informacion_paciente.textLines(info_paciente)
            reporte.drawText(informacion_paciente)

            reporte.drawImage(image=ruta_imc, x=150, y=h-700, width=300, height=250)

            reporte.showPage()
            reporte.save()

            self.txt_mensaje.config(text='Reporte generado con exito.',fg='darkorange')

        except IndexError:
            self.txt_mensaje.config(text='Selecciona un documento', fg='indianred')
