create database crud_poo;
use crud_poo;

create table clientes (idCliente int auto_increment primary key,
nome char(30) not null,
tel char(15),
email char(25) not null,
cidade char(30) default 'Brasilia',
data_cadastro date);

insert into clientes values(null, 'Pedro Antunes','98375-5423','pedro123@gmail.com',default,now());
select * from clientes;