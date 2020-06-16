create table customer2(customer_name varchar(20),customer_id varchar(30) primary key,bill_amount decimal(6,2) not null,prev_balance decimal(6,2) not null,status varchar(30),rem_balance decimal(6,2) not null,plan_id varchar(20))
select * from customer2
create table plans(planid varchar(20) unique,plan_amount decimal(6,2) not null,plan_name varchar(20))
select * from plans
create table customer(name varchar(30),custid varchar(20) primary key,contact_details bigint unique)
select * from customer