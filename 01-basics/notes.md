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
