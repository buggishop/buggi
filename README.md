# buggi

Login as Root in mysql and give following commands;

create user 'django'@'localhost' identified by 'Django@123';

GRANT ALL PRIVILEGES ON *.* TO 'database_user'@'localhost';

Login as django,
Then create each database separately
create database Master;
