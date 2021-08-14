USE gold_trading_platform;

-- CREATING USER TABLE
CREATE TABLE IF NOT EXISTS User (
	user_id INT NOT NULL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL
)ENGINE=INNODB;

-- INSERT ROWS INTO USER TABLE
INSERT INTO User VALUES  
(1, 'admin', '123', 'ghjihad@outlook.com');
