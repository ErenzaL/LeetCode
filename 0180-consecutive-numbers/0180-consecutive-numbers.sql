# Write your MySQL query statement below
SELECT DISTINCT l1.num as ConsecutiveNums
FROM Logs AS l1 INNER JOIN Logs as l2
    ON l1.id = l2.id + 1
    INNER JOIN Logs as l3
    ON l1.id = l3.id -1
WHERE
    l1.num = l2.num and l1.num = l3.num;
