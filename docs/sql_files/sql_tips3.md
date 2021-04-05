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

|SQL Command|Functionality|Example|Pandas Equivalent|
|---|---|---|---|
|LIKE|Search for a specific string pattern|SELECT * FROM info<br>WHERE surname LIKE 'Hatch';|`df.query("surname == 'Hatch'")`|
|ILIKE|Same as LIKE but ignores capitalization|SELECT * FROM info<br>WHERE surname ILIKE 'hatch';|`df.query("surname.str.lower() == 'Hatch'.lower()")`|
|~|Used for matching regular expressions|SELECT * FROM info<br>WHERE surname ~ '[hH]atch';|-|

- Special regex characters when using `LIKE` and `ILIKE`
  - `%` matches 0 or more of any characters
      - `SELECT` * `FROM` info
      `WHERE` surname `LIKE` 'H%';
  - `_` represents a single character (ex// match all names starting with any single character but ending in 'atch')
    - `SELECT` * `FROM` info
      `WHERE` surname `LIKE` '_atch';

### Example (neotoma.westernpollen):

Find out how many `sitename`s have just two words (space separating two words)
- `SELECT` `COUNT`(`DISTINCT` sitename) `FROM` table
  `WHERE` sitename ~ '^\S+\s\S+$';
