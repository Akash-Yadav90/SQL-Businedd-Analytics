# SQL Business Analytics Project

## Overview
This project analyzes retail business data using SQL and SQLite.
It answers 10 business questions related to product revenue,
regional performance, customer behavior, order status, and sales trends.

## Database Tables
- customers: Customer details and regions
- products: Product names, categories, and prices
- orders: Order dates and statuses
- order_items: Products, quantities, and unit prices per order
- payments: Payment amounts, dates, and methods

## Business Questions
1. Which products generate the highest revenue?
2. Which region generates the highest revenue?
3. What is the total revenue for each month?
4. Which customers generate the highest revenue?
5. How many orders exist for each status?
6. What is each customer's revenue rank?
7. What is cumulative monthly revenue?
8. What is the sequence of each customer's orders?
9. What percentage of revenue does each product contribute?
10. Which customers have never placed an order?

## SQL Concepts Used
- SELECT, WHERE, GROUP BY, and ORDER BY
- Aggregate functions: SUM, COUNT, and ROUND
- INNER JOIN and LEFT JOIN
- Common Table Expressions (CTEs)
- Window functions: RANK, ROW_NUMBER, and SUM OVER
- NULL filtering

## Tools
- SQL
- SQLite
- Python
- Visual Studio Code

## How to Run
1. Install Python 3.
2. Run `main.py` to initialize the database.
3. Run `insert_data.py` to insert customers and products.
4. Run `insert_transactions.py` to insert orders and transaction records.
5. Run `python run_query.py` to execute the SQL queries.

## Business Value
The analysis supports revenue tracking, customer segmentation,
product performance analysis, and order management.