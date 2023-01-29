-- Write a script that creates the MySQL server user 


CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY '1';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
