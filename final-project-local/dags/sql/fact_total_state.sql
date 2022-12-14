create table if not exists fact_total_city (
	id serial primary key,
	total_city int not null,
	timestamp timestamp not null
);

insert into fact_total_city (total_city, timestamp)
	select count(office_city),current_timestamp from 
		(select c.office_city from companies c 
			group by c.office_city) as total 

create table if not exists fact_office_per_state (
	id serial primary key,
	state varchar,
	total_office int not null,
	timestamp timestamp not null
);

insert into fact_office_per_state (total_office, state, timestamp)
	select count(office_state_code), office_state_code, current_timestamp  from companies c
		group by c.office_state_code 