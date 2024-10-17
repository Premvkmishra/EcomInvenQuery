# Simplified E-Commerce System and Inventory Management

## Overview

This project is divided into three parts:

1. **System Design**: A simplified e-commerce system that handles users, products, orders, and payments. This includes a class diagram and code stubs.
2. **Business Logic Implementation**: An inventory management system that processes orders, manages stock levels, and handles restocking of products.
3. **Database Query Handling**: SQL queries to retrieve information from a relational database system for an online bookstore.

This repository contains the code for all three parts, including the system design, business logic, and SQL queries.


## How to Run the Code

### Prerequisites

Before running the project, ensure that you have the following installed:

- **Python 3.x**
- **MySQL or PostgreSQL** (or any relational database management system)
- Basic understanding of how to run SQL queries using your preferred database tool (e.g., MySQL Workbench or PostgreSQL command line).

### Steps to Run the Code

1. **Clone the Repository**: Download this repository or unzip the provided archive.

2. **Navigate to the `code/` folder**:
    ```bash
    cd submission/code/
    ```

3. **Running the E-commerce System**:
    - To run the e-commerce system code and see how users, products, orders, and payments are managed, run:
      ```bash
      python ecommerce_system.py
      ```

4. **Running the Inventory Management System**:
    - To run the inventory management system, which processes orders and manages restocking, run:
      ```bash
      python inventory_management.py
      ```

### Running SQL Queries

To run the SQL queries, follow these steps:

1. Open your preferred database management tool (e.g., MySQL Workbench or PostgreSQL).
2. Open the `database_queries.sql` file located in the `queries/` folder.
3. Run each SQL query inside your tool to get the desired results.

The SQL queries will allow you to:
1. Retrieve the top 5 customers who purchased the most books over the last year.
2. Calculate total revenue by each author.
3. Retrieve all books that have been ordered more than 10 times, along with the total quantity ordered.

## Assumptions

Here are some assumptions made during the development of this project:

- **System Design**: Each user can create multiple orders. Each order can contain multiple products. A payment is linked to each order, and the order has various statuses such as pending, completed, or shipped.
  
- **Business Logic**: 
  - When processing orders, the stock levels of products are reduced.
  - If the stock level of a product drops below 10, an alert is triggered for restocking.
  
- **SQL Queries**: 
  - The `Customers` table contains records of all customers in the bookstore.
  - The `Books` table holds book information such as title, author, and price.
  - `Orders` table tracks customer orders, while the `OrderDetails` table tracks the quantity of books ordered in each order.

## Error Handling

- The Python code is designed to handle invalid inputs such as:
  - Processing orders when a product is out of stock.
  - Attempting to restock items without valid quantities.

## System Design Diagram

![Class Diagram](./code/diagrams/class_diagram.png)

This diagram outlines the relationships between `User`, `Product`, `Order`, and `Payment`. It illustrates how these entities interact with each other within the system.

---

Thank you for reviewing this submission! If you have any questions or need clarifications, please feel free to reach out.

