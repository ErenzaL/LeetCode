# Write your MySQL query statement below
SELECT E.name AS Employee
FROM Employee AS E
WHERE EXISTs (
    SELECT 1
    FROM Employee M
    WHERE E.managerId = M.id
    AND E.salary > M.salary
)
