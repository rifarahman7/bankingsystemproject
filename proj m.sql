CREATE DATABASE proj;
USE proj;
CREATE TABLE bank ( account_no INT  PRIMARY KEY, Fname  VARCHAR(30), Pin INT , balance INT );
INSERT INTO bank( account_no,Fname,Pin)
VALUES
(100,'rifa',1234),(101,'jisma',0798),(102,'abi',1111);
select * from bank;
INSERT INTO bank( account_no,Fname,Pin) VALUES
(103,'raas',1234),(104,'scott',0798),(105,'afsal',2222);