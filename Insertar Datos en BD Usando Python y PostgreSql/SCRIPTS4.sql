select 
  id_asesor,
  date_part('day',fecha_gestion) as dia,
  date_part('month',fecha_gestion) as mes,
  (case when tipologia like '%COMPROMISO%' then 'EFECTIVA' 
		when tipologia like '%PRESION%' then 'NO EFECTIVA' 
		when tipologia like '%YA PAGO%' then 'NO EFECTIVA'
		when tipologia like '%NO PAGA%' then 'NO EFECTIVA'
		when tipologia like '%MENSAJE%' then 'NO EFECTIVA'
		when tipologia like '%NO CONTESTA%' then 'NO EFECTIVA'
		when tipologia like '%NUMERO EQUIVOCADO%' then 'NO EFECTIVA'
		when tipologia like '%MENSAJE EN BUZON%' then 'NO EFECTIVA'
		when tipologia like 'M%' then 'NO EFECTIVA'
		when tipologia like '%NO CONTACTADO%' then 'NO EFECTIVA'
		when tipologia like '%NORMALIZADO%' then 'NO EFECTIVA'
		when tipologia like '%SEGUIMIENTO%' then 'NO EFECTIVA'
  end) AS Seguimiento,
   tipologia
   from gestion
    inner join tipologias on
	gestion.id_tipificacion = tipologias.id_tipologia
	group by id_asesor,
			 date_part('day',fecha_gestion),
			 tipologia,
			 id_asesor,
			  date_part('month',fecha_gestion)
	order by id_asesor, dia , mes, tipologia asc
