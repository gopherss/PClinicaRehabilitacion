from database import conexion, consulta

class Pedido:

    numero_pedido: str
    descripcion: str
    fecha: str
    cantidad: float
    precio_unitario: float
    igv: float
    precio_total: float

    def __init__(self, numero_pedido, descripcion, fecha, cantidad, precio_unitario, igv, precio_total):
        self.numero_pedido = numero_pedido
        self.descripcion = descripcion
        self.fecha = fecha
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.igv = igv
        self.precio_total = precio_total
    
    
    def calcular_precio_total(self, cantidad, precio_unitario, igv):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.igv = igv
        porcentaje =  (self.precio_unitario * self.cantidad) * self.igv
        resultado =  (self.precio_unitario * self.cantidad) + porcentaje
        return resultado

    def obtener_pedido(self):
        mi_consulta = consulta.CONSULTAS_PEDIDO['buscar_pedido']
        pedidos = conexion.obtener_datos(consulta=mi_consulta, valores=())
        return pedidos
    
    def nuevo_pedido(self, pedido):
        mi_consulta = consulta.CONSULTAS_PEDIDO['registrar_pedido']
        conexion.crud_datos(consulta=mi_consulta, valores=())
