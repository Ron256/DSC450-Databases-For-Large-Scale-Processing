/****************
Author's Name: Ronaldlee Ejalu
Course: DSC 450
*****************/


CREATE TABLE Animal
(
  AID       NUMBER(3, 0),
  AName      VARCHAR2(30) NOT NULL,
  ACategory VARCHAR2(18),
  TimeToFeed NUMBER(4,2),  
  CONSTRAINT Animal_PK
    PRIMARY KEY(AID)
);

INSERT INTO Animal VALUES(1, 'Galapagos Penguin', 'exotic', 0.5);
INSERT INTO Animal VALUES(2, 'Emperor Penguin', 'rare', 0.75);
INSERT INTO Animal VALUES(3, 'Sri Lankan sloth bear', 'exotic', 2.5);
INSERT INTO Animal VALUES(4, 'Grizzly bear', 'common', 3.0);
INSERT INTO Animal VALUES(5, 'Giant Panda bear', 'exotic', 1.5);
INSERT INTO Animal VALUES(6, 'Florida black bear', 'rare', 1.75);
INSERT INTO Animal VALUES(7, 'Siberian tiger', 'rare', 3.25);
INSERT INTO Animal VALUES(8, 'Bengal tiger', 'common', 2.75);
INSERT INTO Animal VALUES(9, 'South China tiger', 'exotic', 2.5);
INSERT INTO Animal VALUES(10, 'Alpaca', 'common', 0.25);
INSERT INTO Animal VALUES(11, 'Llama', NULL, 3.5);

--Animals that take less than 1.5 hours to feed.
SELECT ANAME 
FROM Animal 
WHERE timetofeed < 1.5;

-- both rare and exotic animals
SELECT AID, ANAME, TIMETOFEED 
FROM Animal
WHERE ACategory = 'rare' OR ACategory = 'exotic';

--List of animals whose rarity is missing in the database
SELECT AID, ANAME, TIMETOFEED 
FROM Animal
WHERE ACategory IS NULL;

--Rarity rating of all animals that require bteween 1 and 2.5 hours to be fed. 
SELECT AID, ANAME FROM Animal
WHERE ACategory = 'rare' 
AND TimeToFeed BETWEEN 1 AND 2.5;
--AND TimeToFeed > 1 AND timetofeed < 2.5;

--Minimum and Maximum feeding time amongst all the animals in the zoo. 
SELECT min(TimeToFeed) AS minimumFeedingTime , max(TimeToFeed) AS maximumFeedingTime FROM Animal;

--Average Feeding Time
SELECT AVG(TimeToFeed) AS AvgFeedingTime 
FROM Animal
WHERE ACategory = 'rare';


--Determining how many NULLS are there in the ACategory column
SELECT COUNT(*) 
FROM  Animal
WHERE ACategory IS NULL;

--all animals named Alpaca, Llama or any other animals that are not listed as exotic
SELECT AID, ANAME, TIMETOFEED FROM Animal
WHERE AName IN ('Alpaca', 'Llama') OR
NOT ACategory = 'exotic';
