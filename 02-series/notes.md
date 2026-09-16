# Lesson 02 — pandas Series

## What is a Series?

A `Series` is a one-dimensional labeled collection of values in pandas.

You can think of it like one column of a table. Each value has an **index**.

```python
import pandas as pd

scores = pd.Series([85, 92, 78])
print(scores)
```

By default, pandas creates indexes `0`, `1`, `2`, and so on.

## Custom indexes

We can give values meaningful labels:

```python
scores = pd.Series(
    [85, 92, 78],
    index=["Amina", "Yusuf", "Hodan"]
)
```

Now we can select a value using its label:

```python
print(scores["Amina"])
```

## Useful things to practice

- Create a Series
- Read its values
- Read its index
- Select one item by label
- Calculate simple statistics such as `mean()`, `min()`, and `max()`

## Key idea

A Series is not just a Python list. It combines **data + an index** and gives us pandas operations for working with that data.
