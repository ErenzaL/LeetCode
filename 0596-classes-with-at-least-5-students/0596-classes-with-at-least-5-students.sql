# Write your MySQL query statement below
SELECT DISTINCT c1.class
FROM Courses AS c1
WHERE (
    SELECT COUNT(*)
    FROM Courses as c2
    WHERE c1.class = c2.class
    GROUP BY class
) >=5