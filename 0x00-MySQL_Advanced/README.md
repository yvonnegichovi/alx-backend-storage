# 0x00. MySQL Advanced

## Description
This project is part of the ALX Backend curriculum. It focuses on advanced MySQL concepts and techniques, such as creating tables with constraints, optimizing queries using indexes, and implementing stored procedures, functions, views, and triggers. 

## Concepts
- Advanced SQL

## Resources
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.sitepoint.com/using-indexes-to-improve-mysql-performance/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/stored-routines.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/views.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives
By the end of this project, you should be able to explain the following without external references:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What stored procedures and functions are and how to implement them in MySQL
- What views are and how to implement them in MySQL
- What triggers are and how to implement them in MySQL

## Requirements
- All scripts will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- Each file should end with a new line
- Each SQL query should have a comment explaining its purpose
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE)
- A `README.md` file at the root of the project folder is mandatory
- The length of your files will be checked using `wc`

## Setup Instructions
1. Use “container-on-demand” to run MySQL.
2. Ask for a container with Ubuntu 18.04 - Python 3.7.
3. Connect via SSH or WebTerminal.
4. Start MySQL in the container:
    ```sh
    $ service mysql start
    ```
5. Import a SQL dump:
    ```sh
    $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
    ```

## Tasks

### 0. We are all unique!
- **File:** `0-uniq_users.sql`
- **Description:** Create a table `users` with `id`, `email`, and `name` attributes, ensuring `email` is unique.

### 1. In and not out
- **File:** `1-country_users.sql`
- **Description:** Create a table `users` with an enumeration for `country`.

### 2. Best band ever!
- **File:** `2-fans.sql`
- **Description:** Rank countries of origin for bands by number of fans.

### 3. Old school band
- **File:** `3-glam_rock.sql`
- **Description:** List all bands with Glam rock as their main style, ranked by longevity.

### 4. Buy buy buy
- **File:** `4-store.sql`
- **Description:** Create a trigger to decrease the quantity of an item after adding a new order.

### 5. Email validation to sent
- **File:** `5-valid_email.sql`
- **Description:** Create a trigger to reset the attribute `valid_email` only when the email has been changed.

### 6. Add bonus
- **File:** `6-bonus.sql`
- **Description:** Create a stored procedure `AddBonus` to add a new correction for a student.

### 7. Average score
- **File:** `7-average_score.sql`
- **Description:** Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student.

### 8. Optimize simple search
- **File:** `8-index_my_names.sql`
- **Description:** Create an index `idx_name_first` on the first letter of the `name` column in the `names` table.

## Author
- Yvonne Ng'endo, Back-End Engineering Student
