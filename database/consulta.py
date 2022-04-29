CONSULTAS_EMPLEADO = {
    'buscar_empleado':
    'SELECT id_empleado, nombre,apellido, tipo, celular, dni, estado, contrasenia FROM empleado;',
    'leer_empleado':
    '''
    SELECT id_empleado, nombre,apellido, tipo, celular, dni, estado, contrasenia 
    FROM empleado WHERE nombre ILIKE %(ILIKE)s ESCAPE '=' or dni  ILIKE %(ILIKE)s ESCAPE '=' ;
    ''',
    'registrar_empleado':
    'INSERT INTO empleado(nombre,apellido,tipo,celular,dni,estado,contrasenia) VALUES(%s,%s,%s,%s,%s,%s,%s);',
    'editar_empleado':
    'UPDATE empleado SET nombre=%s,apellido=%s,tipo=%s,celular=%s,dni=%s,estado=%s,contrasenia=%s WHERE id_empleado=%s;'
}


CONSULTAS_PACIENTE = {
    'buscar_paciente':
    'SELECT id_paciente,nombre,apellido,celular,genero,dni,peso,talla,fecha_nacimiento FROM paciente;',
    'leer_paciente':
    "SELECT id_paciente,nombre,apellido,celular,genero,dni,peso,talla,fecha_nacimiento FROM paciente WHERE nombre ILIKE %(ILIKE)s ESCAPE '=' or dni ILIKE %(ILIKE)s ESCAPE '='",
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
    'leer_historial':
    '''
    select p.nombre, p.apellido,
        p.genero, p.peso, p.talla,
        d.descripcion, t.descripcion, d.created_at,
        p.id_paciente, d.id_diagnostico, t.id_tratamiento
        from paciente as p inner join diagnostico as d 
        on p.id_paciente = d.id_paciente 
        inner join tratamiento as t on p.id_paciente = t.id_paciente
        WHERE p.nombre ILIKE %(ILIKE)s escape '=' or p.dni ILIKE %(ILIKE)s ESCAPE '=';
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
