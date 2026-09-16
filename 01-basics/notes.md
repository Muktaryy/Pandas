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
