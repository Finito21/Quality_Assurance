---
description: "SQL for testers: SELECT queries, filtering, aggregation, JOIN types, NULL pitfalls and checking data in the database while testing an application."
---

# SQL

**SQL (Structured Query Language)** is a language for managing data in **relational databases**. It lets you read, insert, update and delete data and define the database structure (tables, keys, relations).

## Use in a tester's work

- verifying data after **API / ETL** tests,
- checking whether an action in the application **was saved correctly** in the database,
- looking for inconsistencies (duplicates, missing relations, `NULL` values),
- comparing data between environments (test and production),
- preparing **test data** (`INSERT`, `UPDATE`).

!!! note "SQL dialects"
    Syntax differs between databases. `LIMIT 10` works in MySQL, PostgreSQL and SQLite (SQL Server: `SELECT TOP 10`, Oracle: `FETCH FIRST 10 ROWS ONLY`), `AUTO_INCREMENT` is MySQL (PostgreSQL: `GENERATED ... AS IDENTITY`), and `FULL JOIN` does not exist in MySQL. Check the documentation of the database used in your project.

## Basic operations (CRUD)

=== "SELECT"

    ```sql
    SELECT first_name, last_name FROM employees WHERE city = 'Krakow';
    SELECT DISTINCT country FROM customers;   -- unique values
    SELECT * FROM products ORDER BY price DESC LIMIT 10;
    ```

=== "INSERT"

    ```sql
    INSERT INTO employees (first_name, last_name, position)
    VALUES ('John', 'Smith', 'Tester');
    ```

=== "UPDATE"

    ```sql
    UPDATE employees SET position = 'Senior Tester' WHERE id = 7;
    ```

=== "DELETE"

    ```sql
    DELETE FROM employees WHERE id = 7;
    ```

!!! danger "Always with `WHERE`"
    `UPDATE` and `DELETE` without `WHERE` change **every** row in the table. Run a `SELECT` with the same condition first.

!!! warning "Changing data safely"
    Before an `UPDATE` or `DELETE`, run the same condition in a `SELECT`, and make the change in a transaction: `BEGIN; UPDATE ...; SELECT ...;`, then `COMMIT` or `ROLLBACK`. On production use a read-only account only.

## Filtering

| Operator | Meaning | Example |
|---|---|---|
| `=` | equal | `WHERE city = 'Krakow'` |
| `<>` / `!=` | not equal | `WHERE age <> 30` |
| `> < >= <=` | comparisons | `WHERE age > 25` |
| `BETWEEN … AND …` | range | `WHERE age BETWEEN 20 AND 30` |
| `IN (...)` | belongs to a set | `WHERE position IN ('Tester', 'Developer')` |
| `LIKE` | pattern (`%` any string, `_` one character) | `WHERE last_name LIKE 'Smi%'` |
| `IS NULL` / `IS NOT NULL` | empty values | `WHERE email IS NULL` |
| `AND`, `OR`, `NOT` | logic | `WHERE city = 'Krakow' AND position = 'Tester'` |

!!! warning "NULL is not a value"
    - `WHERE email = NULL` never returns anything; use `IS NULL`.
    - `WHERE age <> 30` skips rows where `age` is `NULL`.
    - `NOT IN (subquery)` returns an empty result if the subquery contains a `NULL`; `NOT EXISTS` is safer.
    - `COUNT(column)` skips `NULL`, while `COUNT(*)` counts every row.

## Aggregation

```sql
SELECT COUNT(*)    FROM products;
SELECT SUM(price)  FROM products;
SELECT AVG(price)  FROM products;
SELECT MIN(price), MAX(price) FROM products;

-- grouping + a condition on the group
SELECT position, COUNT(*) AS total
FROM employees
GROUP BY position
HAVING COUNT(*) > 2;
```

## JOINs

| Type | Returns |
|---|---|
| `INNER JOIN` | only matching records from both tables |
| `LEFT JOIN` | all from the left + matching from the right |
| `RIGHT JOIN` | all from the right + matching from the left |
| `FULL JOIN` | all from both (no match gives `NULL`) |

!!! example "INNER JOIN vs LEFT JOIN on data"

    Table `employees`:

    | id | first_name | department_id |
    |---|---|---|
    | 1 | Anna | 10 |
    | 2 | Peter | 20 |
    | 3 | Eve | `NULL` |

    Table `departments`:

    | id | name |
    |---|---|
    | 10 | QA |
    | 20 | Backend |
    | 30 | Frontend |

    ```sql
    SELECT e.first_name, d.name AS department   -- aliases e and d
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id;
    ```

    | first_name | department |
    |---|---|
    | Anna | QA |
    | Peter | Backend |

    The same condition with `LEFT JOIN` also returns Eve, who has no department:

    | first_name | department |
    |---|---|
    | Anna | QA |
    | Peter | Backend |
    | Eve | `NULL` |

    The *Frontend* department does not appear in either result because it has no employees. A `RIGHT JOIN` or `FULL JOIN` would return it.

## Useful queries for testers

```sql
-- duplicate e-mail addresses
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;

-- orders without an existing customer (orphaned records)
SELECT o.* FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;

-- was the order from the test saved correctly
SELECT status, total FROM orders WHERE id = 1234;
```

## Defining the structure

```sql
-- MySQL syntax; in PostgreSQL: id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
CREATE TABLE employees (
  id             INT PRIMARY KEY AUTO_INCREMENT,
  first_name     VARCHAR(50) NOT NULL,
  email          VARCHAR(100) UNIQUE,
  department_id  INT,
  FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
);
```

`ON DELETE CASCADE` means that deleting a parent record also deletes **all related records**, not just the entity itself.
