
-- Drop all the tables to clean up
/*
DROP TABLE Handles;
DROP TABLE Animal;
DROP TABLE ZooKeeper;


CREATE TABLE ZooKeeper
(
  ZID        NUMBER(3,0),
  ZName       VARCHAR2(25) NOT NULL,
  HourlyRate NUMBER(6, 2) NOT NULL,
  
  CONSTRAINT ZooKeeper_PK
     PRIMARY KEY(ZID)
);


-- ACategory: Animal category 'common', 'rare', 'exotic'.  May be NULL
-- TimeToFeed: Time it takes to feed the animal (hours)
CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR(30) NOT NULL,
  ACategory VARCHAR(18),
  
  TimeToFeed NUMBER(4,2),  
  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);


CREATE TABLE Handles
(
  ZooKeepID      NUMBER(3,0),
  AnimalID     NUMBER(3,0),
  
  Assigned     DATE,
  
  CONSTRAINT Handles_PK
    PRIMARY KEY(ZooKeepID, AnimalID),
    
  CONSTRAINT Handles_FK1
    FOREIGN KEY(ZooKeepID)
      REFERENCES ZooKeeper(ZID),
      
  CONSTRAINT Handles_FK2
    FOREIGN KEY(AnimalID)
      REFERENCES Animal(AID)
);


INSERT INTO ZooKeeper VALUES (1, 'Jim Carrey', 500);
INSERT INTO ZooKeeper VALUES (2, 'Tina Fey', 350);  
INSERT INTO ZooKeeper VALUES (3, 'Rob Schneider', 250);
  
INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);

INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);

INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.5);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.25);

INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);



INSERT INTO Handles VALUES(1, 1, '01-Jan-2000');
INSERT INTO Handles VALUES(1, 2, '02-Jan-2000');
INSERT INTO Handles VALUES(1, 10, '01-Jan-2000');

INSERT INTO Handles VALUES(2, 3, '02-Jan-2000');
INSERT INTO Handles VALUES(2, 4, '04-Jan-2000');
INSERT INTO Handles VALUES(2, 5, '03-Jan-2000');

INSERT INTO Handles VALUES(3, 7, '01-Jan-2000');
INSERT INTO Handles VALUES(3, 8, '03-Jan-2000');
INSERT INTO Handles VALUES(3, 9, '05-Jan-2000');
INSERT INTO Handles Values(3, 10,'04-Jan-2000');

*/

--All rare animals  sorted by TimeToFeed
SELECT AID, ANAME, TIMETOFEED FROM Animal
WHERE ACategory = 'rare'
ORDER BY timetofeed;



--Animal names and categories for animals related to a bear. 
SELECT ANAME, ACATEGORY 
FROM Animal 
WHERE AName LIKE '%bear%';


-- Names of the Animals that are related to the tiger and are not common
SELECT ANAME 
FROM Animal
WHERE ANAME LIKE '%tiger%' 
--AND ACATEGORY != 'common';
--AND ACATEGORY <> 'common';
AND NOT ACATEGORY = 'common';


--Names of the animal that are not related to the tiger
SELECT ANAME
FROM Animal
WHERE ANAME --NOT LIKE '%tiger%'
   NOT IN 
        (SELECT ANAME 
        FROM Animal
        WHERE ANAME LIKE '%tiger%')
ORDER BY ANAME;

--List the animals and the ID of the Zoo keeper assigned to them.
SELECT animal.aname, handles.zookeepid 
FROM Animal INNER JOIN handles 
ON (animal.aid = handles.animalid)
ORDER BY animal.aname;

-- A repeat of the previous query that makes sure that the animals 
-- without an assigned handler also appear in the answer 
SELECT animal.aname, handles.zookeepid 
FROM Animal LEFT OUTER JOIN handles 
ON (animal.aid = handles.animalid)
ORDER BY handles.zookeepid;

SELECT * FROM Animal;
SELECT * FROM Zookeeper;
SELECT * FROM Handles;

--Report for every zoo keeper, the average number of hours they spend feeding all animals.
SELECT    zookeeper.zname, AVG(animal.timetofeed) AS AverageNumberOfHrs
FROM zookeeper INNER JOIN  Handles
ON  (handles.zookeepid = zookeeper.zid)
INNER JOIN Animal 
ON (handles.animalid = animal.aid)
GROUP BY zookeeper.zname
ORDER BY AVG(animal.timetofeed);


-- a list of assignment date, zoo keeper name and animal name sorted by assignment date in an ascending order.
SELECT  handles.assigned,  zookeeper.zname, animal.aname
FROM zookeeper INNER JOIN  Handles
ON  (handles.zookeepid = zookeeper.zid)
INNER JOIN Animal 
ON (handles.animalid = animal.aid)
ORDER BY handles.assigned; --By default without specifying ASC, it orders the result set by ascending order from smallest Assigned date to the largest date




