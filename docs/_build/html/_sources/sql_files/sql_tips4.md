# Managing Tables

## Basics

### Creating Tables

- `CREATE`
  - create a new table with x columns
  - `CREATE TABLE` database.new_table_name 
     (
         variable_name `datatype`
         variable_name2 `datatype`
     )

### Data Types

- String Data Types
  - `TEXT(size)` - holds a string
  - `VARCHAR(size)` - variable length string (can contain letters, numbers, special characters), size specifies the max column length in characters
  - `CHAR(size)` - fixed length string (can contain letters, numbers, special characters), size specifies the column length in characters
  - `BINARY(size)` - equal to `CHAR()` but stores binary byte strings, size specifies the column length in bytes
  - `VARBINARY(size)` - equal to `VARCHAR()` but stores binary byte strings, size specifies the max column length in bytes
  - `TEXT(size)` - string (max 65,535 bytes)
  - `LONGTEXT` - string (max 4,294,967,295 characters)
  - `MEDIUMTEXT` - string (max 16,777,215 characters)
  - `TINYTEXT` - string (max 255 characters)
  - `BLOB(size)` - Binary Large OBjects (max 65,535 bytes)
  - `LONGBLOB` - Binary Large OBjects (max 4,294,967,295 bytes)
  - `MEDIUMBLOB` - Binary Large OBjects (max 16,777,215 bytes)
  - `TINYBLOB` - Binary Large OBjects (max 255 bytes)
  - `ENUM(val1, val2, ...)` - string object that can onyl have one value from the list of possible values
  - `SET(val1, val2, ...)` - string object that can have 0 or more values from the list of possible values

- Numeric Data Types

https://www.w3schools.com/sql/sql_datatypes.asp


### Deleting Tables

### Altering Tables

## Setting Constraints

### Setting Keys

### Value Constraints

