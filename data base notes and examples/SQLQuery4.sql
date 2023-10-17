CREATE TABLE Supplier (
S# varchar (5),
SNAME varchar(10),
CITY varchar(10))

CREATE TABLE Part(
P# varchar(5),
PNAME varchar(10),
UNIT int,
COST varchar(5))

CREATE TABLE SP (
Snum varchar(5),
Pnum varchar(5))

CREATE TABLE PopInfo(
Location varchar(10),
Population varchar(10))

SELECT * FROM Supplier
SELECT * FROM Part
SELECT * FROM SP

INSERT INTO Supplier VALUES 
('S1','Smith','London'),
('S2','Jones','Rome'),
('S3','Lee','Tokyo'),
('S4','Poston','Rome'),
('S5','Zhang','London')

INSERT INTO Part VALUES 
('P1','Screw',10,'$100'),
('P2','Hinge',20,'$150'),
('P3','Pin',30,'$200'),
('P4','Nail',40,'$250')

INSERT INTO SP VALUES 
('S1','P1'),
('S1','P3'),
('S2','P1'),
('S2','P2'),
('S1','P2'),
('S3','P1')


 INSERT INTO PopInfo VALUES 
('London','2M'),
('Rome','1.5M'),
('Tokyo','1M'),
('Paris','2.5M')

SELECT SP.Snum,S.SNAME,S.CITY,SP.Pnum,P.PNAME,P.UNIT,P.COST,PP.Population FROM  SP INNER JOIN Supplier AS S  
ON SP.Snum=S.S#
INNER JOIN Part as P
ON SP.Pnum=P.P#
INNER JOIN PopInfo as PP
ON S.CITY=PP.Location

