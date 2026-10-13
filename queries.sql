-- Q1: Which products generate the highest revenue?

SELECT
    p.product_name,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products AS p
JOIN order_items AS oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY
    total_revenue DESC;



    SELECT
    p.product_name,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products AS p
JOIN order_items AS oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC;

-- Q2: Which region generates the highest revenue?

SELECT
    c.region,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
JOIN order_items AS oi
    ON o.order_id = oi.order_id
GROUP BY c.region
ORDER BY total_revenue DESC;


-- Q3: What is the total revenue for each month?
-- Technique: Common Table Expression (CTE)
-- Business Interpretation: Monthly revenue helps identify high-performing months and periods needing improvement.

WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY strftime('%Y-%m', o.order_date)
)
SELECT
    month,
    revenue
FROM monthly_revenue
ORDER BY month;


-- Q4: Which customers generate the highest revenue?
-- Business Interpretation: This query identifies the highest-revenue customers and helps the business prioritize customer retention strategies.

SELECT
    c.customer_id,
    c.customer_name,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
JOIN order_items AS oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_revenue DESC;



-- Q5: How many orders are there for each order status?
-- Business Interpretation: This query helps the business monitor order fulfillment and identify potential processing issues.

SELECT
    status,
    COUNT(*) AS total_orders
FROM orders
GROUP BY status
ORDER BY total_orders DESC;


-- Q6: What is the revenue rank of each customer?
-- Technique: Common Table Expression (CTE) + Window Function

WITH customer_revenue AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers AS c
    JOIN orders AS o
        ON c.customer_id = o.customer_id
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.customer_name
)
SELECT
    customer_id,
    customer_name,
    total_revenue,
    RANK() OVER (ORDER BY total_revenue DESC) AS revenue_rank
FROM customer_revenue
ORDER BY revenue_rank;



-- Q7: What is the cumulative revenue month by month?
-- Technique: CTE + Window Function

-- Business Interpretation: Cumulative revenue helps the business track its overall revenue growth over time.

WITH monthly_revenue AS (
    SELECT
        strftime('%Y-%m', o.order_date) AS month,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders AS o
    JOIN order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY strftime('%Y-%m', o.order_date)
)
SELECT
    month,
    revenue,
    SUM(revenue) OVER (
        ORDER BY month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM monthly_revenue
ORDER BY month;


-- Q8: What is the sequence of orders for each customer?
-- Technique: Window Function (ROW_NUMBER)

-- Business Interpretation: Order sequencing helps the business distinguish first-time purchases from repeat purchases.

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    ROW_NUMBER() OVER (
        PARTITION BY c.customer_id
        ORDER BY o.order_date, o.order_id
    ) AS order_number
FROM customers AS c
JOIN orders AS o
    ON c.customer_id = o.customer_id
ORDER BY c.customer_id, order_number;


-- Q9: What percentage of total revenue does each product contribute?
-- Technique: CTE + Window Function

-- Business Interpretation: Revenue contribution percentages help the business identify products that drive overall sales.

WITH product_revenue AS (
    SELECT
        p.product_id,
        p.product_name,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM products AS p
    JOIN order_items AS oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name
)
SELECT
    product_id,
    product_name,
    total_revenue,
    ROUND(
        100.0 * total_revenue / SUM(total_revenue) OVER (),
        2
    ) AS revenue_percentage
FROM product_revenue
ORDER BY total_revenue DESC;





-- Q10: Which customers have never placed an order?
-- Technique: LEFT JOIN + NULL filtering

-- Business Interpretation: Identifying customers without orders helps the business develop targeted campaigns to encourage their first purchase.

SELECT
    c.customer_id,
    c.customer_name,
    c.region,
    c.signup_date
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.customer_id;
