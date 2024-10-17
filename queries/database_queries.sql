-- SQL Query 1: Top 5 customers who purchased the most books (by total quantity) over the last year
SELECT C.customer_id, C.name, SUM(OD.quantity) AS total_books
FROM Customers C
JOIN Orders O ON C.customer_id = O.customer_id
JOIN OrderDetails OD ON O.order_id = OD.order_id
WHERE O.order_date > NOW() - INTERVAL 1 YEAR
GROUP BY C.customer_id, C.name
ORDER BY total_books DESC
LIMIT 5;

-- SQL Query 2: Total revenue generated from book sales by each author
SELECT B.author, SUM(B.price * OD.quantity) AS total_revenue
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.author
ORDER BY total_revenue DESC;

-- SQL Query 3: Books ordered more than 10 times, along with total quantity ordered
SELECT B.title, SUM(OD.quantity) AS total_ordered
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.title
HAVING total_ordered > 10;
