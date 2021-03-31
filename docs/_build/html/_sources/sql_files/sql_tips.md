# Basics

## Querying Data From a Table

- Basics
  - `SELECT`
  - `FROM`
  - `WHERE` --> conditions (>, <, =, !=, etc.)
  - `DISTINCT`
  - `*`
  - `COUNT`

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

- Renaming columns
  - use `AS` along with `SELECT`
  - can also use `ALTER` but many coding challenges do not allow this
  - `SELECT` table1.Name `AS` 'Customers' `FROM` Customer table1
