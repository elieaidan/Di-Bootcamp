-- create table students (
-- id Serial PRIMARY KEY,
-- last_name varchar (20),
-- first_name varchar (20),
-- birth_date date);

-- insert into students 
-- values
-- (Default,'Marc','Benichou','1998-12-02' ),
-- (Default,'Yoan','Cohen', '2010-12-08' ),
-- (Default,'Lea','Benichou','1987-07-12'),
-- (Default,'Amelia','Dux','1996-04-07'),
-- (Default,'David','Grez','2003-06-14'),
-- (Default,'Omer','Simpson','1980-10-03');


-- insert into students
-- values
-- (Default,'Elie','Aidan','1987-07-12' );

select * from students;
select last_name, first_name from students;
select last_name, first_name from students where id =2;
select last_name, first_name from students 
where last_name = 'Marc' and first_name='Benichou';
select last_name, first_name from students 
where last_name = 'Marc' or first_name='Benichou';
select last_name, first_name from students 
where  last_name like '%a%';

select last_name, first_name from students 
where  last_name like 'a%';
select last_name, first_name from students 
-- where  last_name like '%a';
-- select last_name, first_name from students 
where  last_name like '%a_';
select last_name, first_name from students 
where  id = 1 or id = 3;
select last_name, first_name from students 
where  birth_date > '2002-01-01';








