## Database terminology

- database: a storage area for data collected into tables.
- table: a named collection of records, all with the same structure defined by columns.
- row: a record in a table that represents all the data that takes to describe the entity stored in the table.
- column: a field in a table that all records will have. Columns have a name and a type.
- primary key: a unique id that identifies a single row in a table. This will usually be an auto-incrementing number called `id`, although that is not a requirement of the database.
- SQL: Structured Query Language. A _declarative_ programming language for defining databases and extracting and manipulating information from them.

## SQL

- SQL = Structured Query Language
- When we use Django's ORM, we're using SQL under the hood
- SQL is the language for most relational databases
    - SQLite
    - PostgreSQL
- We can split SQL into two parts
    - Data Definition Language (DDL)
        - CREATE, ALTER, DROP, RENAME
    - Data Manipulation Language (DML)
        - SELECT, INSERT, UPDATE, DELETE

## Creating tables

### The `CREATE TABLE` command

The `CREATE TABLE` command is used to make new database tables. An example:

This example shows the syntax for `CREATE TABLE`.

```sql
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  graduated BOOLEAN NOT NULL DEFAULT 'f',
  cohort INTEGER NOT NULL,
  resume TEXT,
  financial_aid NUMERIC(7,2),
  enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

`CREATE TABLE` takes two arguments: the name of the table and a list of columns. Each column has a name, data type, and options. The columns in the above example explained:

* `id SERIAL PRIMARY KEY`: The `id` column is of type `SERIAL`, which is an integer that is automatically incremented and set when a row is inserted. The option `PRIMARY KEY` says that we will use this column as a unique identifier for each row. This requires that the column is both unique and not nullable.
* `name VARCHAR(100) NOT NULL`: The `name` column is a string with a maximum length of 100 characters. It cannot have a null value.
* `email VARCHAR(100) UNIQUE`: The `email` column is a string with a maximum length of 100 characters. It _can_ be null, but if it has a value, it must be a unique value.
* `graduated BOOLEAN NOT NULL DEFAULT 'f'`: The `graduated` column is a true/false value. It cannot be null, but if you insert a row and do not set the value, it will automatically be set to false.
* `cohort INTEGER NOT NULL`: The `cohort` column is an integer value and cannot be null.
* `resume TEXT`: The `resume` column stores strings of arbitrary length. It can be null.
* `financial_aid NUMERIC(7,2)`: The `financial_aid_per_year` column is a decimal value with precision (total number of digits) of 7 and scale (digits right of the decimal point) of 2. It can be null.
* `enrolled_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP`: The `enrolled_at` column is a date and time value and cannot be null. If not specified, the current date and time are used.

There are more datatypes for columns, including complex ones that can hold multiple values. Some of the common simple ones are:

* REAL (floating point number)
* DATE
* TIME
* INTERVAL (amount of time)

### Deleting tables

To delete a table, use `DROP TABLE <tablename>`. If you want PostgreSQL to not throw an error if the table does not exist -- this is a nice thing to put at the top of a schema definition file -- use `DROP TABLE IF EXISTS <tablename>`.

### References

* ["Data Definition" from the PostgreSQL manual](https://www.postgresql.org/docs/9.6/static/ddl.html)
* ["Data Types" from the PostgreSQL manual](https://www.postgresql.org/docs/9.6/static/datatype.html)
* [`CREATE TABLE` syntax](https://www.postgresql.org/docs/9.6/static/sql-createtable.html)
* [`DROP TABLE` syntax](https://www.postgresql.org/docs/9.6/static/sql-droptable.html)

## Inserting data

### The `INSERT INTO` command

The `INSERT INTO` command adds rows to an existing database table. Some examples:

```sql
INSERT INTO students (name, email, graduated, cohort) VALUES ('Charlie', 'charlie@example.org', 't', 1);
INSERT INTO students (name, email, cohort) VALUES ('Harper', 'harper@example.org', 12);
INSERT INTO students (name, cohort, financial_aid)
VALUES
('Kelly', 12, 1000),
('Alexis', 12, 1500.50);
```

The `INSERT INTO` command takes a table name, a set of columns, the keyword `VALUES`, and one or more sets of values to insert into the specified set of columns. You can forgo the set of columns if your values contain values for every column, in the order they exist in the table.

### Other ways to insert data

If you have bulk data in a text or CSV file, you can add it using the `COPY` command, the `\copy` directive in the PostgreSQL shell, or a third-party tool like [pgloader](http://pgloader.io/) or [pgAdmin 3](https://www.pgadmin.org/). You can also insert data from most programming languages.

### References

* ["Inserting data" from the PostgreSQL manual](https://www.postgresql.org/docs/9.6/static/dml-insert.html)
* [`INSERT INTO` syntax](https://www.postgresql.org/docs/9.6/static/sql-insert.html)
* [`COPY` syntax](https://www.postgresql.org/docs/9.6/static/sql-copy.html)

## Selecting, updating, and deleting data

### The `SELECT` command

The `SELECT` command is used to retrieve data from a table. In its simplest form, it looks like this:

```sql
SELECT * FROM students;
```

This command will select all columns and all rows from the `students` table.

The columns can be filtered like so:

```sql
SELECT id, name, email FROM students;
```

### Filtering rows with `WHERE`

The `SELECT` command can have a clause starting with `WHERE` to specify conditions used to filter the rows returned. To get only students who have graduated, for example, you can write:

```sql
SELECT * FROM students WHERE graduated = 't';
```

Besides equality, there are the usual operators, like `>`, `>=`, `<`, and `<=`. There are also the operators `IS NULL` and `IS NOT NULL`, which you use instead of the equality operator to see if a field is null or not. Some examples:

```sql
-- Find all the students with no email
SELECT name
  FROM students
 WHERE email IS NULL;

-- Find students with $1000 or more in financial aid
SELECT *
  FROM students
 WHERE financial_aid >= 1000.00;
```

Conditions can be combined with `AND` and `OR` and parentheses can be used to ensure precedence.

```sql
-- Find students that have graduated but have no resumé
SELECT name
  FROM students
 WHERE graduated = 't'
   AND resume IS NULL;

-- Find students that have graduated or are in the most recent cohorts
SELECT name, cohort
  FROM students
 WHERE graduated = 't'
    OR cohort >= 10;
```

### Sorting with `ORDER BY`

The `ORDER BY` clause is used to sort the returned rows from `SELECT`. It takes one or more columns as arguments, optionally suffixed with `DESC` to specify descending order.

```sql
-- Students from least financial aid to most
  SELECT name
       , financial_aid
    FROM students
ORDER BY financial_aid;

-- Students from most financial aid to least
  SELECT name
       , financial_aid
    FROM students
ORDER BY financial_aid DESC;

-- Get rid of the nulls
  SELECT name
       , financial_aid
    FROM students
   WHERE financial_aid IS NOT NULL
ORDER BY financial_aid DESC;
```

### `LIMIT` and `OFFSET`

The `LIMIT` clause can be used to limit the number of rows that are returned from a `SELECT`. The `OFFSET` clause is used to skip a number of rows.

```sql
-- Get the top 5 students receiving financial aid
  SELECT name
       , financial_aid
    FROM students
   WHERE financial_aid IS NOT NULL
ORDER BY financial_aid DESC
   LIMIT 5;

-- Get the students 6-10
  SELECT name
       , financial_aid
    FROM students
   WHERE financial_aid IS NOT NULL
ORDER BY financial_aid DESC
   LIMIT 5
  OFFSET 5;   
```

### Updating data with `UPDATE`

The `UPDATE` command updates data in a table. By default, all rows are updated, which is usually not what you want. To prevent this, use a `WHERE` clause to limit the rows affected.

```sql
-- Graduate cohort 11.
UPDATE students
   SET graduated = 't'
 WHERE cohort = 11;
```

### Deleting data with `DELETE`

Like `UPDATE`, `DELETE` affects all rows. Use a `WHERE` clause to limit the rows affected.

```sql
-- Delete all students without an email.
DELETE FROM students
      WHERE email IS NULL;
```

### References

* [PostgreSQL SELECT documentation](https://www.postgresql.org/docs/9.6/static/sql-select.html)
* [PostgreSQL UPDATE documentation](https://www.postgresql.org/docs/9.6/static/sql-update.html)
* [PostgreSQL DELETE documentation](https://www.postgresql.org/docs/9.6/static/sql-delete.html)

## Aggregations and Functions

SQL provides functions and clauses for us to manipulate our result set from `SELECT` statements. Some of the most common functions are used for aggregations.

### COUNT

`COUNT()` is used to get a count of rows. In its simplest form, we use it to find out how many rows are in a table.

```sql
SELECT COUNT(*) FROM movies;
```

### GROUP BY

`COUNT()` becomes much more powerful with the `GROUP BY` clause. This allows us to split our result set by one of more columns before aggregating. We can use it to get a count of the records with one or more columns in common. Note that we _cannot_ use an unaggregated column in our `SELECT` statement without putting it in the `GROUP BY` clause.

```sql
-- Number of movies by studio
SELECT studio, COUNT(*) AS count
FROM movies
GROUP BY studio
ORDER BY count DESC;
```

### SUM, AVG, MIN, and MAX

`SUM()`, `AVG()`, `MIN()`, and `MAX()` aggregate a particular column and return a result.

```sql
-- Average movie run length
SELECT AVG(runtime_in_minutes) FROM movies;

-- Average movie budget by studio
SELECT studio, AVG(budget_in_millions) AS avg_budget
FROM movies
GROUP BY studio
ORDER BY avg_budget DESC;

-- Average profit by studio
SELECT studio, AVG(revenue_in_millions - budget_in_millions) AS avg_profit
FROM movies
GROUP BY studio
ORDER BY avg_profit DESC;
```

### ROUND

`ROUND()` is an example of a SQL function that does not aggregate, but works on each value in a column.

```sql
-- Average profit by studio
SELECT studio, 
  ROUND(AVG(revenue_in_millions - budget_in_millions), 3) AS avg_profit
FROM movies
GROUP BY studio
ORDER BY avg_profit DESC;
```

### EXTRACT

`EXTRACT()` is another SQL function that does not aggregate. It works on timestamp, date, time, and interval values and can pull out subfields from those values, letting you get, for example, the year or day of week from a date value.

```sql
-- Average profit by year
SELECT EXTRACT(year FROM release_date) AS year,
  ROUND(AVG(revenue_in_millions - budget_in_millions), 3) AS avg_profit
FROM movies
GROUP BY year
ORDER BY year;
```
### References

* [Functions and Operators](https://www.postgresql.org/docs/9.6/static/functions.html)
* [Aggregate Functions](https://www.postgresql.org/docs/9.6/static/functions-aggregate.html)
* [Date/Time Functions](https://www.postgresql.org/docs/9.6/static/functions-datetime.html)

## Foreign Keys and Joins

When we think about data, we find relationships naturally forming out of that data. Some examples:

- A publisher has many books
- A studio has many movies
- A person has one or more email addresses
- A book has one or more authors
- An author has one or more books
- A movie has one or more actors
- An actor has one or more movies
- A student has many classes
- A class has many students

We can use a relational database like PostgreSQL to store these relationships in multiple tables.

### What is a foreign key?

A _foreign key_ is used to connect tables to form these relationships. Here is a simplified table structure for movies and studios:

```sql
CREATE TABLE studios (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  studio_id INTEGER NOT NULL REFERENCES studios(id)
);
```

The `movies` table has a column, `studio_id`, that references the `id` column from `studios`. Each entry in the `studio_id` column should be an id from the `studios` table. We say that a movie _belongs to_ a studio or _has one_ studio, while a studio _has many_ movies.

When you have a relationship like actors and movies -- a movie has many actors; an actor has many movies -- you use a _join table_.

```sql
CREATE TABLE actors (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL
);

CREATE TABLE movie_actors (
  movie_id INTEGER NOT NULL REFERENCES movies(id),
  actor_id INTEGER NOT NULL REFERENCES actors(id)
);
```

We say that an actor _has and belongs to many_ movies, or a movie _has and belongs to many actors_.

### Joins

To connect tables, we use the `JOIN` clause with `SELECT` statements. Let's see an example:

```sql
SELECT movies.title, studios.name AS studio
FROM movies
JOIN studios ON movies.studio_id = studios.id;
```

```
-[ RECORD 1 ]-------------------------------------------------------------------------------------------------------
title  | Visions of Europe
studio | Megascreen Filmworks
-[ RECORD 2 ]-------------------------------------------------------------------------------------------------------
title  | Spring is Here
studio | Megascreen Filmworks
-[ RECORD 3 ]-------------------------------------------------------------------------------------------------------
title  | 10th & Wolf
studio | Jast Studios
```

There's a lot to unpack in this one statement. First, see the `AS` clause after `studios.name`. We can use `AS` in several contexts to give a new name to a value. Then, look at the `JOIN` clause. We state a table we want to join to our table from our `FROM` clause, and then use `ON` to specify the condition on which it should be joined.

This style of join is called an _inner join_. With an inner join, only rows that have a match on both sides of the `ON` clause are displayed. If we had movies with no `studio_id`, they would not appear, and if a movie had a `studio_id` that did not have an `id` in the `studios` table, that row would also not appear. This is often what we want, but not always.

Imagine we have movies that might not have a studio, but we want them to show up anyway in our list. First, let's see a query with an inner join:

```sql
UPDATE movies SET studio_id = NULL WHERE id = 183;

SELECT movies.id, movies.title, studios.name AS studio
FROM movies
JOIN studios ON movies.studio_id = studios.id
LIMIT 2;

-- -[ RECORD 1 ]----------------
-- id     | 49
-- title  | Visions of Europe
-- studio | Megascreen Filmworks
-- -[ RECORD 2 ]----------------
-- id     | 474
-- title  | 10th & Wolf
-- studio | Jast Studios
```

Now, let's use a _left join_, where all rows on the left side of our join show up:

```sql
SELECT movies.id, movies.title, studios.name AS studio
FROM movies
LEFT JOIN studios ON movies.studio_id = studios.id
LIMIT 2;

-- -[ RECORD 1 ]----------------
-- id     | 49
-- title  | Visions of Europe
-- studio | Megascreen Filmworks
-- -[ RECORD 2 ]----------------
-- id     | 183
-- title  | Spring is Here
-- studio | 
```

`RIGHT JOIN` and `FULL JOIN` also exist, allowing for all rows on the right side of the join, or all rows on both sides of the join respectively.

### Why design databases this way?

Database theory is outside of the scope of this class, but you should read up on database normalization for more info.

### References

* [A Visual Representation of SQL Joins](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins)
* ["Joins Between Tables" from the PostgreSQL documentation](https://www.postgresql.org/docs/9.6/static/tutorial-join.html)
* [An introduction to database normalization](http://phlonx.com/resources/nf3/)
