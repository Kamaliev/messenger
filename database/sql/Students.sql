drop table Students;
create table Students(
    id  integer primary key ,
    first_name text,
    last_name text,
    login text UNIQUE ,
    password text,
    time datetime,
    online datetime
);

select * from Students;
delete from Events where id >0;
insert into Students (first_name, last_name, login, password) Values ('Равиль', 'Камалиев', 'sihnel', '123456');
update Students set online = '123123213' where