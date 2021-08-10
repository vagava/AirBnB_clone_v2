--- Create databases  hbnb_test_db
--- Create user hbnb_test and grant privileges on hbnb_test_db
--- Grant privileges to hbnb_test on performance_schema

CREATE DATABASE IF NOT EXISTS
    hbnb_test_db;
USE  hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY  'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO  hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO  hbnb_test@localhost;
FLUSH PRIVILEGES;
