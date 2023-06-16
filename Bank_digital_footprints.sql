drop table if exists agreement_digital_footprints;
create table agreement_digital_footprints as (
select 
	l.loan_id as contract_id,
	'Loan' as product,
	l.customer_id,
	l.open_date,
	c.call_id as digital_footprint_id,
	c.call_dttm as digital_footprint_dttm,
	case 
		when c.incom_outcom = 'incoming'
		then 'Incoming Call'
		else 'Outcoming Call'
	end as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from loan l 
inner join calls c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.call_result = 'positive'
		and c.offer_product = 'loan'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.card_id as contract_id,
	'Card' as product,
	l.customer_id,
	l.open_date,
	c.call_id as digital_footprint_id,
	c.call_dttm as digital_footprint_dttm,
	case 
		when c.incom_outcom = 'incoming'
		then 'Incoming Call'
		else 'Outcoming Call'
	end as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from card l 
inner join calls c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.call_result = 'positive'
		and c.offer_product = 'card'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.loan_id as contract_id,
	'Loan' as product,
	l.customer_id,
	l.open_date,
	c.visit_id as digital_footprint_id,
	c.visit_dttm as digital_footprint_dttm,
	'Office Visit' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from loan l 
inner join office_visits c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.visit_aim = 'consult'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.card_id as contract_id,
	'Card' as product,
	l.customer_id,
	l.open_date,
	c.visit_id as digital_footprint_id,
	c.visit_dttm as digital_footprint_dttm,
	'Office Visit' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from card l 
inner join office_visits c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.visit_aim = 'consult'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.contract_id as contract_id,
	'Deposit' as product,
	l.customer_id,
	l.open_date,
	c.visit_id as digital_footprint_id,
	c.visit_dttm as digital_footprint_dttm,
	'Office Visit' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from deposit_contract l 
inner join office_visits c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.visit_aim = 'consult'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0
	
union all 

select 
	l.insurance_id as contract_id,
	'Insurance' as product,
	l.customer_id,
	l.open_date,
	c.visit_id as digital_footprint_id,
	c.visit_dttm as digital_footprint_dttm,
	'Office Visit' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from insurance l 
inner join office_visits c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c.visit_aim = 'consult'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0
	
union all 

select 
	l.loan_id as contract_id,
	'Loan' as product,
	l.customer_id,
	l.open_date,
	c.activity_id as digital_footprint_id,
	c.activity_dttm as digital_footprint_dttm,
	'Online Bank' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from loan l 
inner join internet_activity c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c."RESULT" = 'view'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.card_id as contract_id,
	'Card' as product,
	l.customer_id,
	l.open_date,
	c.activity_id as digital_footprint_id,
	c.activity_dttm as digital_footprint_dttm,
	'Online Bank' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from card l 
inner join internet_activity c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c."RESULT" = 'view'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0

union all 

select 
	l.contract_id,
	'Deposit' as product,
	l.customer_id,
	l.open_date,
	c.activity_id as digital_footprint_id,
	c.activity_dttm as digital_footprint_dttm,
	'Online Bank' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from deposit_contract l 
inner join internet_activity c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c."RESULT" = 'view'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0
	
union all 

select 
	l.insurance_id as contract_id,
	'Insurance' as product,
	l.customer_id,
	l.open_date,
	c.activity_id as digital_footprint_id,
	c.activity_dttm as digital_footprint_dttm,
	'Online Bank' as digital_footprint_type,
	cast(current_date as timestamp) as processed_dttm
from insurance l 
inner join internet_activity c 
	on 1=1
		and l.customer_id = c.customer_id 
		and c.eff_to_dttm = '2999-12-31 00:00:00'
		and c.deleted_flg = 0
		and c."RESULT" = 'view'
where 1=1
	and l.eff_to_dttm = '2999-12-31 00:00:00'
	and l.deleted_flg = 0
);


--select * from agreement_digital_footprints


