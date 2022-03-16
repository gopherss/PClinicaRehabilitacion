from database import conexion, consulta


class Diagnostico:

    diagnostico: str
    tratamiento: str

    def __init__(self, diagnostico, tratamiento):
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

    def obtener_historial(self):
        mi_consulta = consulta.CONSULTAS_DIAGNOSTICO['buscar_historial']
        historial = conexion.obtener_datos(consulta=mi_consulta, valores=())
        return historial

    def nuevo_diagnostico(self, mi_objeto, id_paciente):
        mi_consulta_uno = consulta.CONSULTAS_DIAGNOSTICO['registrar_diagnostico']
        mi_consulta_dos = consulta.CONSULTAS_DIAGNOSTICO['registrar_tratamiento']

        conexion.crud_datos(consulta=mi_consulta_uno, valores=(
            mi_objeto.diagnostico, id_paciente))
        conexion.crud_datos(consulta=mi_consulta_dos, valores=(
            mi_objeto.tratamiento, id_paciente))

    def actualizar_diagnostico(self, mi_objeto, id_diagnostico, id_tratamiento):
        mi_consulta_uno = consulta.CONSULTAS_DIAGNOSTICO['editar_diagnostico']
        mi_consulta_dos = consulta.CONSULTAS_DIAGNOSTICO['editar_tratamiento']

        conexion.crud_datos(consulta=mi_consulta_uno, valores=(
            mi_objeto.diagnostico, id_diagnostico))
        conexion.crud_datos(consulta=mi_consulta_dos, valores=(
            mi_objeto.tratamiento, id_tratamiento))
