USE gold_trading_platform;

-- CREATING USER TABLE
CREATE TABLE IF NOT EXISTS User (
	user_id INT NOT NULL PRIMARY KEY,
	username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    type VARCHAR(20) NOT NULL DEFAULT 'user'
)ENGINE=INNODB;


-- CREATEING ORDERS TABLE
-- order status (0: not validated, 1: validated)
-- delivery_type (0: physical, 1:virtual)
CREATE TABLE IF NOT EXISTS Orders (
	order_id INT NOT NULL PRIMARY KEY,
    quantity INT NOT NULL,
    price FLOAT NOT NULL,
    order_date DATETIME NOT NULL,
    order_status CHAR(1) NOT NULL,
    -- order_type (sell/buy)
    delivery_status VARCHAR(50) NOT NULL,
    delivery_type CHAR(1) NOT NULL,
    user_id INT NOT NULL,
    
    CONSTRAINT Orders_FK FOREIGN KEY (user_id) REFERENCES USer(user_id)
)ENGINE=INNODB;


-- INSERT ROWS INTO USER TABLE
INSERT INTO User VALUES
 (1, 'admin', '123', 'test@gmail.com', 'admin');

-- 
DROP TABLE Orders;
SELECT * FROM Orders;
SELECT * FROM User;



