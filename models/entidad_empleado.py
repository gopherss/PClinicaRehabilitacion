from database import conexion, consulta


class Empleado:

    nombre: str
    apellido: str
    tipo: str
    celular: str
    dni: str
    estado: bool
    contrasenia: str

    def __init__(self, nombre, apellido, tipo, celular, dni, estado, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        self.celular = celular
        self.dni = dni
        self.estado = estado
        self.contrasenia = contrasenia

    def obtener_empleado(self):
        mi_consulta = consulta.CONSULTAS_EMPLEADO['buscar_empleado']
        empleados = conexion.obtener_datos(consulta=mi_consulta, valores=())
        return empleados

    def leer_empleado(self, informacion):
        mi_consulta = consulta.CONSULTAS_EMPLEADO['leer_empleado']
        empleados = conexion.leer_datos(
            consulta=mi_consulta, valores=informacion)
        return empleados

    def nuevo_empleado(self, empleado):
        mi_consulta = consulta.CONSULTAS_EMPLEADO['registrar_empleado']
        conexion.crud_datos(consulta=mi_consulta, valores=(empleado.nombre, empleado.apellido,
                            empleado.tipo, empleado.celular, empleado.dni, empleado.estado, empleado.contrasenia))

    def remover_empleado(self, id_empleado):
        mi_consulta = consulta.CONSULTAS_EMPLEADO['eliminar_empleado']
        conexion.crud_datos(consulta=mi_consulta, valores=(id_empleado,))

    def actualizar_empleado(self, empleado, id_empleado):
        mi_consulta = consulta.CONSULTAS_EMPLEADO['editar_empleado']
        conexion.crud_datos(consulta=mi_consulta, valores=(empleado.nombre, empleado.apellido, empleado.tipo,
                            empleado.celular, empleado.dni, empleado.estado, empleado.contrasenia, id_empleado))
