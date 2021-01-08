CREATE TABLE public.deudores
(
    identificacion integer NOT NULL,
    nombre varchar(80) COLLATE pg_catalog."default" NOT NULL,
    estado boolean NOT NULL,
    CONSTRAINT identificacion_pkey PRIMARY KEY (identificacion)
	
)


CREATE TABLE public.asignaciones
(
    id_asignacion SERIAL NOT NULL,
	identificacion integer NOT NULL,
	id_obligacion integer NOT NULL,
	saldo_a_capital money NOT NULL,
	saldo_actual money NOT NULL,
	saldo_en_mora money NOT NULL,
	dias_mora integer NOT NULL,
	unidad integer NOT NULL,
    CONSTRAINT id_asignacion_pk PRIMARY KEY (id_asignacion)
	
)

ALTER TABLE public.asignaciones
add constraint unidad_fk foreign key(unidad) references unidades(id_unidad)


CREATE TABLE public.tipologias
(
    id_tipologia SERIAL NOT NULL,
	tipologia  VARCHAR(50) NOT NULL,
    contactabilidad VARCHAR(50) NOT NULL,
	efectividad VARCHAR(50) NOT NULL,
	CONSTRAINT id_tipologia_pk PRIMARY KEY (id_tipologia)
)

CREATE TABLE public.asesores
(
    identificacion integer NOT NULL,
    nombres varchar(50)  NOT NULL,
    fecha_ingreso date NOT NULL,
	estado bool NOT NULL,
	unidad integer NOT NULL,
    CONSTRAINT identificacion_pk PRIMARY KEY (identificacion)
)


CREATE TABLE public.gestion
(
    id_gestion SERIAL NOT NULL,
    id_asesor integer  NOT NULL,
	fecha_gestion date NOT NULL,
	Hora_gestion time NOT NULL,
	identificacion_deudor integer NOT NULL,
	id_tipificacion integer NOT NULL,
    CONSTRAINT id_gestion PRIMARY KEY (id_gestion),
	CONSTRAINT id_asesor_fk FOREIGN KEY(id_asesor) references asesores(identificacion)
)



alter table public.gestion 
add constraint tipificacion_fk foreign key(id_tipificacion) references tipologias(id_tipologia);
alter table public.gestion 
add constraint id_deudor_fk foreign key(identificacion_deudor) references deudores(identificacion);
