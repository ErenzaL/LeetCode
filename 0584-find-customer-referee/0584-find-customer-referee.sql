# Write your MySQL query statement below
SELECT c1.name 
FROM Customer as c1
WHERE EXISTS(
    SELECT c2.name
    FROM Customer as c2
    WHERE c1.id = c2.id
    AND c1.referee_id <>2 OR c1.referee_id IS NULL
)