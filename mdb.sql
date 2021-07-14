CREATE DATABASE phonebook;

USE phonebook;

CREATE TABLE phonebook(
`id` int(5) auto_increment NOT NULL primary key,
`login` varchar(15) NOT NULL,
`password` varchar(15) NOT NULL,
`phone_num` varchar(100) NOT NULL,
`bd` varchar(15)
);

insert into `phonebook`(`login`,`password`,`phone_num`,`bd`) VALUES ('admin','password','+79999999999','09.11.2001');

select * from phonebook;