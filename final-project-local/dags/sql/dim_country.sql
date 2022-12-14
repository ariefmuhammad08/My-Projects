create table if not exists dim_country (
	id serial primary key,
	country_code varchar not null
);

truncate table dim_country restart identity cascade;

insert into dim_country (country_code)
	select office_country_code from companies
	group by office_country_code