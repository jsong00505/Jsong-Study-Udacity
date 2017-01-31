# Deeper into SQL

## Normalized Design

In a **normalized** database, the relationships among the tables match the relationships that are really there among the data.

1. Every row has the same number of columns.
2. There is a unique **key**, and everything in a row says something about the key.
3. Facts that don't relate to the key belong in different tables.
4. Tables shouldn't imply relationships that don't exist.

## Create Table and Types

```SQL
  create table tablename (
    column1 type [contraints],
    column2 type [contraints],
    ...
  );
```

* Some systems support abbreviations for long type names.

> timestamptz      = timestamp with time zone
> (PostgreSQL only)  (SQL standarad type name)
>
> Look for more in the PostgreSQL documentation!

## Creating and Dropping

create database name [options];
drop database name [options];
drop table name [options];

## Declaring Primary Keys

#### only one primary key

```SQL
  create table students(
    id serial primary key,
    name text,
    birthdate date
  );
```

#### multiple primary keys

```SQL
  create table postal_places (
    postal_code text,
    country text,
    name text,
    primary key (postal_code, country)
  );
```

## Declaring Relationships

```SQL
  create table sales (
    sku text references products,
    sale_date date,
    count integer
  );

  sku: Stock Keeping Unit
```

**references** provides referential integrity - columns that are supposed to refer to each other are guaranteed to do so.

## Foreign Keys

A **foreign key** is a column or set of columns in one table, that uniquely identifies rows in another table.

```SQL
create table students (
  id serial primary key,
  name text
);

create table courses (
  id text primary key,
  name text
);

create table grades (
  student integer references students (id),
  course text references courses (id),
  grade text
);
```

![foreign-keys-1](../lesson4-pic/foreign-keys-1.png)

![foreign-keys-2](../lesson4-pic/foreign-keys-2.png)
