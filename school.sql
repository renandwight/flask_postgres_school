DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Teachers;
DROP TABLE IF EXISTS Subjects;

CREATE TABLE Subjects(
    id SERIAL PRIMARY KEY,
    subject VARCHAR(50)
);

CREATE TABLE Students(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT REFERENCES subjects (id)
);

CREATE TABLE Teachers(
    id SERIAL PRIMARY KEY, 
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    age INT,
    subject INT REFERENCES subjects (id)
);

\COPY subjects FROM './data/subjects.csv' DELIMITER ',' CSV HEADER;
\COPY students FROM './data/student.csv' DELIMITER ',' CSV HEADER;
\COPY teachers FROM './data/teachers.csv' DELIMITER ',' CSV HEADER;

SELECT * FROM students;
SELECT * FROM teachers;
SELECT * FROM subjects;
