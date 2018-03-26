.read lab12.sql

CREATE TABLE sp17favnum AS
  SELECT number, COUNT(*) AS count FROM sp17students GROUP BY number ORDER BY count DESC LIMIT 1;


CREATE TABLE sp17favpets AS
  SELECT pet, COUNT(*) AS count FROM sp17students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count FROM students GROUP BY pet ORDER BY count DESC LIMIT 10;


CREATE TABLE fa17dog AS
  SELECT pet, COUNT(*) AS count FROM students WHERE pet = 'dog';


CREATE TABLE fa17alldogs AS
  SELECT pet, COUNT(*) AS count FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, hilfinger, COUNT(*) AS count FROM students WHERE seven = '7' GROUP BY denero, hilfinger;

CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count FROM students GROUP BY smallest ORDER BY smallest ASC;
