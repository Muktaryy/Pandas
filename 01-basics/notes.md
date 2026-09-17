# 01 — pandas Basics

## What I will learn

- What pandas is and why it is useful.
- How to import pandas with `import pandas as pd`.
- How pandas represents tabular data.
- The difference between a Series and a DataFrame.
- How to create my first small DataFrame.

## Notes

I will add my own notes here as I learn each concept.

## What is a Series?

A Series is like one column of data.

### Example

```python
import pandas as pd

ages = pd.Series([20, 25, 30])

print(ages)
```

### Why do we use it?

A Series is useful when we have one-dimensional data, such as ages, names, or prices.

## Series Attributes

A Series has attributes that help us understand its data.

### Example

```python
print(ages.dtype)
print(ages.shape)
print(ages.size)
```

- `dtype` tells us the data type.
- `shape` tells us the number of rows.
- `size` tells us the total number of values.

These attributes are useful when exploring data before working with it.

## Series Indexing

Indexing lets us access a specific value in a Series by its position.

### Example

```python
print(ages.iloc[0])
print(ages.iloc[1])
print(ages.iloc[2])
```

The positions start at `0`, so for `[20, 25, 30]`:

- position `0` → `20`
- position `1` → `25`
- position `2` → `30`

`iloc` is useful when we want to access data by its integer position.

## Series Labels

A Series can also have custom labels instead of only using the default integer index.

### Example

```python
ages = pd.Series([20, 25, 30], index=["Ali", "Asha", "Omar"])

print(ages["Ali"])
print(ages["Omar"])
```

The labels make it easier to identify values by name.

- `Ali` → `20`
- `Asha` → `25`
- `Omar` → `30`

Labels are useful when the index represents meaningful information, such as names or IDs.

## DataFrame Basics

A DataFrame is a two-dimensional table with rows and columns.

Think of a DataFrame like a small spreadsheet:

- columns represent different pieces of information
- rows represent individual records

### Example

```python
students = pd.DataFrame({
    "name": ["Ali", "Asha", "Omar"],
    "age": [20, 25, 30]
})

print(students)
```

This creates a table with two columns: `name` and `age`.

### Why do we use it?

Most real-world datasets are tables. DataFrames make it easier to inspect, filter, clean, and analyze that tabular data.

A simple way to remember the difference:

- **Series** → one column
- **DataFrame** → multiple columns and rows

## Selecting DataFrame Columns

After creating a DataFrame, we often need only one or a few columns.

### Select one column

```python
print(students["name"])
```

Selecting one column returns a **Series**.

### Select multiple columns

```python
print(students[["name", "age"]])
```

Selecting multiple columns returns a **DataFrame**.

The important difference is the brackets:

- `students["name"]` → one column → Series
- `students[["name", "age"]]` → multiple columns → DataFrame

Column selection is useful because real datasets often contain many columns, but we may only need a few for our analysis.

## Filtering DataFrame Rows

After selecting the columns we need, we often want only the rows that match a condition.

### Example

```python
adults = students[students["age"] >= 25]

print(adults)
```

Here, `students["age"] >= 25` creates a True/False condition for each row.

Pandas then uses that condition to keep only the rows where the condition is `True`.

In this example:

- Ali → `20 >= 25` → `False` → removed
- Asha → `25 >= 25` → `True` → kept
- Omar → `30 >= 25` → `True` → kept

Filtering is important because real datasets can contain thousands or millions of rows, and we often need to analyze only the records that match a specific condition.
