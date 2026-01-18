{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 /*\
  -----------------------------------------------------------------------\
  Project: Database Design & Management (The Pet Hotel)\
  Description: End-to-end simulation of creating and managing a relational database.\
  Skills: DDL (Create/Drop), DML (Insert/Update/Delete), Constraints.\
  Author: Jesse Tamayo\
  -----------------------------------------------------------------------\
*/\
\
-- 1. SCHEMA DESIGN (DDL)\
-- Dropping legacy tables and creating a robust structure with constraints.\
\
DROP TABLE IF EXISTS Pets;\
\
CREATE TABLE Pets (\
    PetID INT PRIMARY KEY,       -- Unique Identifier\
    Name VARCHAR(50) NOT NULL,   -- Validation: Name is required\
    Type VARCHAR(50),\
    Weight DECIMAL(5, 2)         -- Precision math for weight\
);\
\
-- 2. DATA POPULATION (DML)\
-- Inserting multiple rows in a single optimized transaction.\
\
INSERT INTO Pets (PetID, Name, Type, Weight)\
VALUES \
    (101, 'Max', 'Dog', 30.00),\
    (102, 'Luna', 'Cat', 4.50);\
\
-- 3. DATA MAINTENANCE\
-- Updating records based on new information (Max gained weight).\
\
UPDATE Pets\
SET Weight = 32.50\
WHERE PetID = 101;\
\
-- 4. RECORD REMOVAL\
-- Removing a pet that has checked out (Luna).\
\
DELETE FROM Pets\
WHERE PetID = 102;}