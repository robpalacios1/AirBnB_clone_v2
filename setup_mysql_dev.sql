--prepares a MySQL server for this project
Create DATABASE if NOT EXISTS hbnb_dev_db;
Create USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `perfomance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
