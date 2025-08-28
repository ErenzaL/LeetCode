# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers as c
WHERE NOT EXISTS (
    SELECT customerId
    FROM Orders AS o
    WHERE o.customerId = c.id
)
