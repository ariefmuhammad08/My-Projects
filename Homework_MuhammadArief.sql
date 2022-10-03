-- buat tabel
create table ref_customers(
	cust_id integer,
	cust_nm varchar,
primary key (cust_id)
);

create table ref_products(
	prd_id integer,
	prd_nm varchar,
primary key (prd_id)
);

create table trx_transactions(
	trx_id integer,
	cust_id integer,
	prd_id integer,
	qty integer,
	price integer,
primary key (trx_id),
foreign key (cust_id) references ref_customers(cust_id) on delete cascade,
foreign key (prd_id) references ref_products(prd_id) on delete cascade
);

-- insert data
insert into ref_customers 
values 
	(1,'Marzuq'),
	(2,'Markus');

insert into ref_products 
values
	(1,'ABC'),
	(2,'XYZ'),
	(3,'QWE');

insert into trx_transactions 
values
	(1,1,1,10,30000),
	(2,1,2,20,20000),
	(3,1,3,5,10000),
	(4,2,1,5,15000),
	(5,2,2,5,1000);

-- jawaban soal
-- 1
select 
	cus.cust_nm,
	sum(qty) as total_qty
from trx_transactions as trx
join ref_customers as cus
	on trx.cust_id = cus.cust_id 
group by 1;

-- 2
select 
	prod.prd_nm,
	sum(price) as total_price
from trx_transactions as trx
join ref_products as prod
	on trx.prd_id = prod.prd_id 
group by 1;


