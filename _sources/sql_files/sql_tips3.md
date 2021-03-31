# Operators

## SQL Operators

### Combining Queries

- `UNION`
  - combines rows from two queries
  - `SELECT` col1, col2, `FROM` table1
    `UNION` 
    `SELECT` col1, col2, `FROM` table2

- `INTERSECT`
  - returns common rows from two queries
  - `SELECT` col1, col2 `FROM` table1
    `INTERSECT`
    `SELECT` col1, col2, `FROM` table2

- `MINUS`
  - subtracts a result set from another result set

### LIKE, ILIKE, NOT LIKE, ETC.

