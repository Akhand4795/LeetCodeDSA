/* Write your T-SQL query statement below */
SELECT
    Students.student_id, Students.student_name, Subjects.subject_name, COUNT(Examinations.student_id) AS attended_exams
FROM
    Students
CROSS JOIN
    Subjects
LEFT JOIN
    Examinations
ON
    Students.student_id = Examinations.student_id
AND
    Examinations.subject_name = Subjects.subject_name
GROUP BY
    Students.student_id, Students.student_name, Subjects.subject_name, Examinations.student_id, Examinations.subject_name;;