DROP DATABASE IF EXISTS phonebook;
CREATE DATABASE phonebook;

USE phonebook;

CREATE TABLE users(
`id` int(5) auto_increment NOT NULL primary key,
`login` varchar(15) NOT NULL,
`password` varchar(15) NOT NULL,
`bd` varchar(15) NOT NULL
);
CREATE Table phonebook(
`id` int(5) auto_increment NOT NULL primary key,
`user_id` int (5) NOT NULL,
`name` varchar(100) NOT NULL,
`phone_num` varchar(20) NOT NULL,
`bd` varchar(15) NOT NULL,
FOREIGN KEY(`user_id`) REFERENCES users(`id`)
);

insert into `users`(`login`,`password`,`bd`) VALUES ('admin','password','09.11.2001');

select * from users;
