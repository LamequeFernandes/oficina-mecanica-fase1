CREATE USER 'lameque'@'localhost' IDENTIFIED BY 'lameque123';

GRANT ALL PRIVILEGES ON *.* TO 'lameque'@'localhost' WITH GRANT OPTION;

CREATE USER 'lameque'@'%' IDENTIFIED BY 'lameque123';

GRANT ALL PRIVILEGES ON *.* TO 'lameque'@'%' WITH GRANT OPTION;
