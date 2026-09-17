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

## Sorting DataFrame Rows

After filtering data, we may want to arrange the rows in a specific order.

### Sort by one column

```python
sorted_students = students.sort_values("age")

print(sorted_students)
```

By default, `sort_values()` sorts the values from **smallest to largest** (ascending order).

### Sort in descending order

```python
sorted_students = students.sort_values("age", ascending=False)

print(sorted_students)
```

`ascending=False` changes the order to **largest to smallest**.

Sorting is useful when we want to find things like the oldest students, highest scores, or cheapest products more easily.

## Missing Data

Real-world datasets often contain missing values. For example, a student may have no recorded age or score.

In pandas, missing values are commonly represented by `NaN`.

### Example

```python
students = pd.DataFrame({
    "name": ["Ali", "Asha", "Omar"],
    "age": [20, None, 30]
})

print(students)
```

Here, Asha's age is missing.

### Find missing values

```python
print(students.isna())
```

`isna()` checks each value and returns:

- `True` → the value is missing
- `False` → the value is present

We can also count missing values in each column:

```python
print(students.isna().sum())
```

This is an important first step in data cleaning because missing values can affect our analysis.


## Cleaning Missing Data

Finding missing values is only the first step. When data is missing, we need to decide what to do with it.

### Remove rows with missing values

```python
clean_students = students.dropna()

print(clean_students)
```

`dropna()` removes rows that contain missing values.

For example, if Asha has no age, her row will be removed.

### Fill missing values

Sometimes we do not want to remove the row. We can replace the missing value with another value.

```python
students["age"] = students["age"].fillna(0)

print(students)
```

`fillna(0)` replaces missing values with `0`.

The value we choose depends on the meaning of the data. We should not blindly replace missing values without thinking about what makes sense for the dataset.

### Why cleaning matters

Real-world data is rarely perfect. Cleaning helps us prepare data before analysis so that missing values do not produce misleading results.
