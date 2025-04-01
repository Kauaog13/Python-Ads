create database db_senac;
use db_senac;

create table usuario(coduser int auto_increment primary key,
nome char(30) not null,
senha varchar(30) not null,
cidade char(30) not null default 'Brasilia');

show tables;

select * from usuario;

insert into usuario values(null, 'Arnaldo', 'senac123',default);
insert into usuario values(null, 'Fonseca', 'senac123',default);	
insert into usuario values(null, 'Jose', 'senac123','São Paulo');
insert into usuario values(10, 'Ana Paula', 'senac123','Ceilandia');
insert into usuario values(null, 'Paula', 'senac123',default);

describe usuario;
select * from usuario;