from database import conexion, consulta
from math import pow


class Paciente:

    nombre: str
    apellido: str
    celular: str
    genero: str
    dni: str
    peso: float
    talla: float
    fecha_nacimiento: str

    def __init__(self, nombre, apellido, celular, genero, dni, peso, talla, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.genero = genero
        self.dni = dni
        self.peso = peso
        self.talla = talla
        self.fecha_nacimiento = fecha_nacimiento

    def obtener_paciente(self):
        mi_consulta = consulta.CONSULTAS_PACIENTE['buscar_paciente']
        pacientes = conexion.obtener_datos(consulta=mi_consulta, valores=())
        return pacientes

    def nuevo_paciente(self, paciente, id_empleado):
        mi_consulta = consulta.CONSULTAS_PACIENTE['registrar_paciente']
        conexion.crud_datos(consulta=mi_consulta, valores=(
            paciente.nombre, paciente.apellido, paciente.celular,
            paciente.genero, paciente.dni, paciente.peso,
            paciente.talla, paciente.fecha_nacimiento, id_empleado
        ))

    def actualizar_paciente(self, paciente, id_paciente, id_empleado):
        mi_consulta = consulta.CONSULTAS_PACIENTE['editar_paciente']
        conexion.crud_datos(consulta=mi_consulta, valores=(
            paciente.nombre, paciente.apellido, paciente.celular,
            paciente.genero, paciente.dni, paciente.peso,
            paciente.talla, paciente.fecha_nacimiento, id_empleado,
            id_paciente
        ))

    def calcular_imc(self, peso, talla):
        imc = peso / pow(talla, 2)
        return round(imc,2)
