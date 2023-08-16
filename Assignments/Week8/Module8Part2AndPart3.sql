
/***********
Part 2
***********/
/*
DROP TABLE STUDENT CASCADE CONSTRAINTS;
CREATE TABLE STUDENT(
	ID		CHAR(3),
	Name		VARCHAR2(20),
	Midterm	NUMBER(3,0) 	CHECK (Midterm>=0 AND Midterm<=100),
	Final		NUMBER(3,0)	CHECK (Final>=0 AND Final<=100),
	Homework	NUMBER(3,0)	CHECK (Homework>=0 AND Homework<=100),
	PRIMARY KEY (ID)
);
INSERT INTO STUDENT VALUES ( '445', 'Seinfeld', 86, 90, 99 );
INSERT INTO STUDENT VALUES ( '909', 'Costanza', 74, 72, 86 );
INSERT INTO STUDENT VALUES ( '123', 'Benes', 93, 89, 91 );
INSERT INTO STUDENT VALUES ( '111', 'Kramer', 99, 91, 93 );
INSERT INTO STUDENT VALUES ( '667', 'Newman', 78, 82, 84 );
INSERT INTO STUDENT VALUES ( '889', 'Banya', 50, 65, 50 );
SELECT * FROM STUDENT;

DROP TABLE WEIGHTS CASCADE CONSTRAINTS;
CREATE TABLE WEIGHTS(
	MidPct	NUMBER(2,0) CHECK (MidPct>=0 AND MidPct<=100),
	FinPct	NUMBER(2,0) CHECK (FinPct>=0 AND FinPct<=100),
	HWPct	NUMBER(2,0) CHECK (HWPct>=0 AND HWPct<=100)
);
INSERT INTO WEIGHTS VALUES ( 30, 30, 40 );
SELECT * FROM WEIGHTS;
COMMIT;

*/
/***********************************************************************************************
Author: Ronaldlee Ejalu
Course: DSC 450
*Function that derives final letter grade
************************************************************************************************/
/*
SET SERVEROUTPUT ON;
CREATE OR REPLACE function computeGradeFn(inMidPct  NUMBER, inFinPct NUMBER, inHwPct NUMBER)
RETURN CHAR as
    vMidPct NUMBER(4) := 0;
    vFinPct NUMBER(4) := 0;
    vHwPct  NUMBER(4)  := 0;
    vOverallScore  NUMBER := 1.0;
    vGrade CHAR(1) := 'A';
BEGIN
    SELECT MidPct, FinPct, HWPct INTO vMidPct, vFinPct, vHwPct
    FROM WEIGHTS;
    vOverallScore := inMidPct * (vMidPct/100) + inFinPct * (vFinPct/100) + inHwPct * (vHwPct/100);
    --dbms_output.put_line('The overallscore is '|| vOverallScore);     -- This is for debugging purposes
    CASE
        WHEN vOverallScore BETWEEN 90 AND 100   THEN vGrade := 'A';
        WHEN vOverallScore BETWEEN 80 AND 89.99 THEN vGrade := 'B';
        WHEN vOverallScore BETWEEN 65 AND 79.99 THEN vGrade := 'C';
        ELSE vGrade := 'F';
    END CASE;
    return vGrade;
END;
/
*/
/***********************************************************************************************
Author: Ronaldlee Ejalu
Course: DSC 450
*Function that computes the overall score
************************************************************************************************/
/*
CREATE OR REPLACE function computeOverallScoreFn(inMidPct  NUMBER, inFinPct NUMBER, inHwPct NUMBER)
RETURN NUMBER as
    vMidPct NUMBER(4) := 0;
    vFinPct NUMBER(4) := 0;
    vHwPct  NUMBER(4)  := 0;
    vOverallScore  NUMBER := 1.0;
BEGIN
    SELECT MidPct, FinPct, HWPct INTO vMidPct, vFinPct, vHwPct
    FROM WEIGHTS;
    return (inMidPct * (vMidPct/100) + inFinPct * (vFinPct/100) + inHwPct * (vHwPct/100)); 
END;
/
*/

/*
SET SERVEROUTPUT ON;
*/
/********************************************
* Author: Ronaldlee Ejalu
* DSC 450
* An anonymous PL/SQL block.
*********************************************/
/*
DECLARE
    -- declare a cursor
    cursor student_cursor IS 
        (SELECT ID, 
                NAME, 
                MIDTERM, 
                FINAL, 
                HOMEWORK 
        FROM Student);
    -- declare variables
    v_id Student.ID%TYPE;
    v_name Student.NAME%TYPE;
    v_midterm NUMBER;
    v_final NUMBER;
    v_homework NUMBER;
    v_midpct Weights.midpct%TYPE;
    v_finpct Weights.finpct%TYPE;
    v_hwpct Weights.hwpct%TYPE;
    v_lettergrade CHAR(1);
BEGIN
    SELECT MidPct, FinPct, HWPct 
    INTO v_midpct, v_finpct, v_hwpct
    FROM WEIGHTS;
    DBMS_OUTPUT.put_line('Weights are '||v_midpct ||', '|| v_finpct ||', '||v_hwpct);
    --open the cursor
    OPEN student_cursor;
    Loop
    --retrieve each row of the result of the bove query into PL/SQL variables
    FETCH student_cursor INTO v_id, v_name, v_midterm, v_final, v_homework;
    EXIT WHEN student_cursor%NOTFOUND;
    --This is for debugging purposes
    --DBMS_OUTPUT.PUT_LINE(v_midterm ||' '|| v_final || ' '|| v_homework); 
    DBMS_OUTPUT.put_line(v_id ||' ' ||v_name ||' '||computeoverallscorefn(v_midterm, v_final, v_homework) ||' '||computegradefn(v_midterm, v_final, v_homework));
    END Loop;
    --Free the cursor used by query
    CLOSE student_cursor;
END;
*/

/************
Part 3
*************/
DROP TABLE ENROLLMENT CASCADE CONSTRAINTS;
DROP TABLE SECTION CASCADE CONSTRAINTS;
CREATE TABLE SECTION(
 SectionID 	CHAR(5),
 Course	VARCHAR2(7),
 Students	NUMBER DEFAULT 0,
 CONSTRAINT PK_SECTION 
		PRIMARY KEY (SectionID)
);

CREATE TABLE ENROLLMENT(
 SectionID	CHAR(5),
 StudentID	CHAR(7),
 CONSTRAINT PK_ENROLLMENT 
		PRIMARY KEY (SectionID, StudentID),
 CONSTRAINT FK_ENROLLMENT_SECTION 
		FOREIGN KEY (SectionID)
		REFERENCES SECTION (SectionID)
);
 
INSERT INTO SECTION (SectionID, Course) VALUES ( '12345', 'CSC 355' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '22109', 'CSC 309' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99113', 'CSC 300' );
INSERT INTO SECTION (SectionID, Course) VALUES ( '99114', 'CSC 300' );
COMMIT;
SELECT * FROM SECTION;

--Sample Data:
SET SERVEROUTPUT ON;
INSERT INTO ENROLLMENT VALUES ('12345', '1234567');
INSERT INTO ENROLLMENT VALUES ('12345', '2234567');
INSERT INTO ENROLLMENT VALUES ('12345', '3234567');
INSERT INTO ENROLLMENT VALUES ('12345', '4234567');
INSERT INTO ENROLLMENT VALUES ('12345', '5234567');
INSERT INTO ENROLLMENT VALUES ('12345', '6234567');
SELECT * FROM Section;
SELECT * FROM Enrollment;


SELECT COUNT(*)
--, SECTIONID 
FROM Enrollment 
--GROUP BY SECTIONID;
WHERE sectionid = '123498';

SET SERVEROUTPUT ON;
/****************************************************
* Author: Ronaldlee Ejalu
* Course: DSC 450
* A trigger that fires when a user attempts to insert a row into enrollment.
* This checks the value of the Section.Students for the corresponding section.
* If the section students is lesss than 5, there is still room in the section to allow the insert and update Section.Students table
or else the section is full so it cancels the insert and display the error message 
*****************************************************/
CREATE OR REPLACE TRIGGER checkStudentsEnroll_BR
BEFORE INSERT ON Enrollment
FOR EACH ROW
DECLARE
    -- declare the number of students variable
    v_CntOfStudents section.students%TYPE;
    v_numberOfStudents section.students%TYPE;
    
BEGIN
    SELECT 
            COUNT(*) INTO v_CntOfStudents
    FROM Enrollment 
    WHERE sectionid = :new.SectionID;
    
    -- we need to add 1 since there are section id without any entries in the enrollment table
    v_numberOfStudents := v_CntOfStudents + 1;
      
    -- this is for debugging purposes   
    -- DBMS_OUTPUT.PUT_LINE('Number of Students before insert  is ' || v_numberofstudents); 
    IF v_numberofstudents > 5 THEN  
        raise_application_error(-20102, 'The section is full, can not insert more students into enrollments table');
        
    ELSIF v_numberofstudents <= 5 THEN
        UPDATE SECTION 
        SET students = v_numberofstudents 
        WHERE SectionID = :new.SectionID;
    
    END IF;
END;
/



/**********************************************************************
*Author Ronaldlee Ejalu
*DSC 450
* A trigger that fires when a user attempts to delete one or more rows from the Enrollment table.
* It updates the values the Section.Students for any affected sections by decreasing the value
* of Section.Students by one each time a student is removed from a section. 
***********************************************************************/
CREATE OR REPLACE TRIGGER attemptDelEnrollment_BR
BEFORE DELETE ON ENROLLMENT
FOR EACH ROW
BEGIN
    UPDATE SECTION
    SET students = students - 1
    WHERE sectionid = :old.sectionid;
END;
/
--testing the trigger
DELETE FROM ENROLLMENT WHERE StudentID = '1234567';
commit;
SELECT * FROM Section;
SELECT * FROM Enrollment;

