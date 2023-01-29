-- Write a script that creates the MySQL server user user_0d_1.
--      user_0d_1 should have all privileges on your MySQL server
--      The user_0d_1 password should be set to user_0d_1_pwd
--      If the user user_0d_1 already exists, your script should not fail

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';
