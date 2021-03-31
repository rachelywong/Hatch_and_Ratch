# SQL Cheatsheet

## Querying Data From a Table

- Basics
  - `SELECT`
  - `FROM`
  - `WHERE`
  - `DISTINCT`
  - `*`

- Ordering By
  - `SELECT` col1, col2 `FROM` table
  `ORDER BY` col `ASC`
  - can say `DESC` 

  - `SELECT` col1, col2 `FROM` table
  `ORDER BY` col `LIMIT` 1 `OFFSET` 1
  - limit = how many rows, offset = skip rows

- Group By --> must aggregate or use some condition like having
  - aggregate = (`COUNT()`, `MAX()`, `MIN()`, `SUM()`, `AVG()`)
 
  - `SELECT` col1 `aggregate` col2
    `FROM` table
    `GROUP BY` col1

  - `SELECT` col1 `aggregate` col2
    `FROM` table
    `GROUP BY` col1
    `HAVING` condition