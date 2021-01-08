CREATE TABLE public.clientes
(
    identificacion_cliente integer NOT NULL,
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    fecha_registro date NOT NULL,
    estado boolean NOT NULL,
    CONSTRAINT clientes_pkey PRIMARY KEY (identificacion_cliente)
)


CREATE TABLE public.unidades
(
    id_unidad SERIAL NOT NULL,
    nombre_unidad character varying(50) COLLATE pg_catalog."default" NOT NULL,
    estado boolean NOT NULL,
    CONSTRAINT unidades_pkey PRIMARY KEY (id_unidad)
	)

CREATE TABLE unidad_cliente(
     
	id_unidad_cliente SERIAL NOT NULL,
	id_cliente integer NOT NULL,
	id_unidad integer NOT NULL,
    CONSTRAINT id_unidad_cliente_pkey PRIMARY KEY (id_unidad_cliente),
	CONSTRAINT identificacion_cliente_fk FOREIGN KEY (id_cliente) references clientes(identificacion_cliente),    
	CONSTRAINT id_unidad_fk FOREIGN KEY (id_unidad) references unidades(id_unidad)
)
