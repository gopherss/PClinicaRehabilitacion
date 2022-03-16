CREATE DATABASE dbclinica;


-- \c dbclinica;

CREATE TABLE proveedor
(
    id_proveedor SERIAL NOT NULL,
    nombre VARCHAR(90) NOT NULL,
    celular VARCHAR(10) NOT NULL,
    direccion VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_proveedor_pk PRIMARY KEY(id_proveedor)
);

INSERT INTO proveedor(nombre,celular,direccion) 
VALUES ('Tottus','986532752','Calle. las orquideas, #33'),
('Saga fallabella','926523752','Calle. las orquideas, #100'),
('Ripley','946599752','Mall Aventura Plaza, #99'),
('Oechle!','996510752','Mall Aventura Plaza, #02');

CREATE TABLE empleado
(
    id_empleado SERIAL NOT NULL,
    nombre VARCHAR(90) NOT NULL,
    apellido VARCHAR(90) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    celular VARCHAR(9) NOT NULL,
    dni VARCHAR(8) NOT NULL,
    estado BOOLEAN NOT NULL DEFAULT TRUE,
    contrasenia TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_empleado_pk PRIMARY KEY(id_empleado)
);

INSERT INTO empleado(nombre,apellido,tipo,celular,dni,estado, contrasenia)
VALUES ('Jeiner','Espinoza','Administrador','986532651','74748595',TRUE,'1324653'),
('Roberto','Gomez','Empleado','986532666','74448510',FALSE,'894655');


CREATE TABLE pedido
(
    id_pedido SERIAL NOT NULL,
    numero_pedido VARCHAR(90) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    id_empleado INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_pedido_pk PRIMARY KEY(id_pedido),
    CONSTRAINT id_empleado_fk FOREIGN KEY(id_empleado)
        REFERENCES empleado
);

INSERT INTO pedido(numero_pedido,descripcion,fecha,id_empleado)
VALUES('PE01','Crema par las articulaciones','2022-01-18',1);


CREATE TABLE detalle_pedido
(
    id_detalle_pedido SERIAL NOT NULL,
    cantidad NUMERIC(9,2) NOT NULL,
    precio_unitario NUMERIC(9,2) NOT NULL,
    igv NUMERIC(9,2) NOT NULL,
    precio_total NUMERIC(9,2) NOT NULL,
    id_pedido INTEGER NOT NULL,
    id_proveedor INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_detalle_pedido_pk PRIMARY KEY(id_detalle_pedido),
    CONSTRAINT id_pedido_fk FOREIGN KEY(id_pedido)
        REFERENCES pedido,
    CONSTRAINT id_proveedor_fk FOREIGN KEY(id_proveedor)
        REFERENCES proveedor
);

INSERT INTO detalle_pedido(cantidad,precio_unitario,igv,precio_total,id_pedido,id_proveedor)
VALUES(10,80,0.18,800,1,1);


--Tablas Para Crear el Historial Médico

CREATE TABLE paciente
(
    id_paciente SERIAL NOT NULL,
    nombre VARCHAR(90) NOT NULL,
    apellido VARCHAR(90) NOT NULL,
    celular VARCHAR(9) NOT NULL,
    genero VARCHAR(1) NOT NULL,
    dni VARCHAR(8) NOT NULL,
    peso NUMERIC(9,2) NOT NULL,
    talla NUMERIC(9,2) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
	id_empleado INTEGER NOT NULL,
    created_at  TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_paciente_pk PRIMARY KEY(id_paciente),
    CONSTRAINT id_empleado_fk FOREIGN KEY(id_empleado)
        REFERENCES empleado
);

INSERT INTO paciente(nombre,apellido,celular,genero,dni,peso,talla,fecha_nacimiento,id_empleado)
VALUES('Sandro','Castro','985656263','M','74176171',70,1.70,'19/07/1998',1);


CREATE TABLE diagnostico
(
    id_diagnostico SERIAL NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    id_paciente INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_diagnostico_pk PRIMARY KEY(id_diagnostico),
    CONSTRAINT id_paciente_fk FOREIGN KEY(id_paciente)
        REFERENCES paciente
);

INSERT INTO diagnostico(descripcion,id_paciente)
VALUES('Ligamentos debiles',1);


CREATE TABLE tratamiento
(
    id_tratamiento SERIAL NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    id_paciente INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    CONSTRAINT id_tratamiento PRIMARY KEY(id_tratamiento),
    CONSTRAINT id_paciente_fk FOREIGN KEY(id_paciente)
        REFERENCES paciente
);

INSERT INTO tratamiento(descripcion,id_paciente)
VALUES('Masajes Cada 3 dias durante 1 mes ',1);

