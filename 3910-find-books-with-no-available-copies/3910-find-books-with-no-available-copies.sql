# Write your MySQL query statement below
WITH borrow as
(SELECT book_id, COUNT(*) as current_borrowers
FROM borrowing_records
WHERE return_date IS NULL
GROUP BY book_id)

SELECT l.book_id, 
    title, 
    author,
    genre, 
    publication_year,
    b.current_borrowers
FROM library_books as l
LEFT JOIN borrow as b
ON b.book_id = l.book_id
WHERE l.total_copies = current_borrowers
ORDER BY current_borrowers DESC, title ASC


