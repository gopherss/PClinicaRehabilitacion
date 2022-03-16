from database import conexion, consulta


class Proveedor:

    nombre: str
    celular: str
    direccion: str

    def __init__(self, nombre, celular, direccion):
        self.nombre = nombre
        self.celular = celular
        self.direccion = direccion
    
    def obtener_proveedor(self):
        mi_consulta = consulta.CONSULTAS_PROVEEDOR['buscar_proveedor']
        proveedores =  conexion.obtener_datos(consulta=mi_consulta, valores=())
        return proveedores
    
    def nuevo_proveedor(self, proveedor):
        mi_consulta = consulta.CONSULTAS_PROVEEDOR['registrar_proveedor']
        conexion.crud_datos(consulta=mi_consulta, valores=(proveedor.nombre,proveedor.celular,proveedor.direccion))
    
    def remover_proveedor(self, id_proveedor):
        mi_consulta = consulta.CONSULTAS_PROVEEDOR['eliminar_proveedor']
        conexion.crud_datos(consulta=mi_consulta, valores=(id_proveedor,))
    
    def actualizar_proveedor(self, proveedor, id_proveedor):
        mi_consulta = consulta.CONSULTAS_PROVEEDOR['editar_proveedor']
        conexion.crud_datos(consulta=mi_consulta, valores=(proveedor.nombre, proveedor.celular, proveedor.direccion, id_proveedor))

