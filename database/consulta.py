CONSULTAS_PROVEEDOR = {
    'buscar_proveedor':
    'SELECT id_proveedor, nombre, celular, direccion, created_at FROM proveedor;',
    'registrar_proveedor':
    'INSERT INTO proveedor(nombre,celular,direccion) VALUES(%s,%s,%s);',
    'eliminar_proveedor':
    'DELETE FROM proveedor WHERE id_proveedor=%s;',
    'editar_proveedor':
    'UPDATE proveedor SET nombre=%s, celular=%s, direccion=%s WHERE id_proveedor = %s;'
}

CONSULTAS_EMPLEADO = {
    'buscar_empleado':
    'SELECT id_empleado, nombre,apellido, tipo, celular, dni, estado, contrasenia FROM empleado;',
    'registrar_empleado':
    'INSERT INTO empleado(nombre,apellido,tipo,celular,dni,estado,contrasenia) VALUES(%s,%s,%s,%s,%s,%s,%s);',
    'eliminar_empleado':
    'DELETE FROM empleado WHERE id_empleado=%s;',
    'editar_empleado':
    'UPDATE empleado SET nombre=%s,apellido=%s,tipo=%s,celular=%s,dni=%s,estado=%s,contrasenia=%s WHERE id_empleado=%s;'
}

CONSULTAS_PEDIDO = {
    'buscar_pedido':
    'SELECT pe.id_pedido, pe.numero_pedido, pe.descripcion, pe.fecha, dt.cantidad, dt.precio_unitario, dt.igv, dt.precio_total FROM pedido as pe join detalle_pedido as dt on pe.id_pedido = dt.id_pedido;',
    'registrar_pedido':
    'INSERT INTO pedido (numero_pedido,descripcion,fecha,id_empleado) VALUES(%s,%s,%s,%s);',
    'registrar_detalle_pedido':
    'INSERT INTO detalle_pedido (cantidad,precio_unitario,igv,precio_total,id_pedido,id_proveedor) VALUES(%s,%s,%s,%s,%s,%s);'
}

CONSULTAS_PACIENTE = {
    'buscar_paciente':
    'SELECT id_paciente,nombre,apellido,celular,genero,dni,peso,talla,fecha_nacimiento FROM paciente;',
    'registrar_paciente':
    'INSERT INTO paciente(nombre,apellido,celular,genero,dni,peso,talla,fecha_nacimiento,id_empleado) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);',
    'editar_paciente':
    'UPDATE paciente SET nombre=%s, apellido=%s, celular=%s, genero=%s, dni=%s, peso=%s, talla=%s, fecha_nacimiento=%s, id_empleado=%s WHERE id_paciente=%s;'
}


CONSULTAS_DIAGNOSTICO = {
    'buscar_historial':
    '''
    select p.nombre, p.apellido,
        p.genero, p.peso, p.talla,
        d.descripcion, t.descripcion, d.created_at,
        p.id_paciente, d.id_diagnostico, t.id_tratamiento
        from paciente as p inner join diagnostico as d 
        on p.id_paciente = d.id_paciente 
        inner join tratamiento as t on p.id_paciente = t.id_paciente;
    ''',
    'registrar_diagnostico':
    'INSERT INTO diagnostico (descripcion, id_paciente) VALUES(trim(%s),%s);',
    'registrar_tratamiento':
    'INSERT INTO tratamiento (descripcion, id_paciente) VALUES(trim(%s),%s);',
    'editar_diagnostico':
    'UPDATE diagnostico set descripcion=trim(%s) WHERE id_diagnostico=%s',
    'editar_tratamiento':
    'UPDATE tratamiento set descripcion=trim(%s) WHERE id_tratamiento=%s'
}
