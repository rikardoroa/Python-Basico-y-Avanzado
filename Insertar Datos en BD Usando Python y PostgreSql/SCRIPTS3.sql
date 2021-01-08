CREATE TABLE public.obligaciones
(
    id_obligacion SERIAL NOT NULL,
    estado integer  NOT NULL,
    CONSTRAINT id_obligacion_pkey PRIMARY KEY (id_obligacion)
)




CREATE TABLE public.pagos
   (
    id_obligacion integer  NOT NULL,
    valor money NOT NULL,
	fecha date NOT NULL
	)
	
alter table public.pagos
add CONSTRAINT pagos_obligacion_fk FOREIGN KEY(id_obligacion) references obligaciones(id_obligacion)


alter table public.asignaciones
add CONSTRAINT pagos_obligacion_fk FOREIGN KEY(id_obligacion) references obligaciones(id_obligacion)
