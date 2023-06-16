drop table if exists agreement_channel;
create table agreement_channel as (
with prep as (
	select 
		l.contract_id,
		l.product,
		l.customer_id,
		l.open_date,
		l.digital_footprint_id,
		l.digital_footprint_dttm,
		l.digital_footprint_type,
		row_number() over (partition by l.contract_id, l.product order by l.digital_footprint_dttm asc) as r_n,
		cast(current_date as timestamp) as processed_dttm
	from agreement_digital_footprints l 
	where 1=1
)
select 
	contract_id,
	product,
	customer_id,
	open_date,
	digital_footprint_id,
	digital_footprint_dttm,
	digital_footprint_type,
	processed_dttm
from prep 
where 1=1
	and r_n = 1
);

--select * from agreement_channel
