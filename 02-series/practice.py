"""Lesson 02: Practice with pandas Series."""

import pandas as pd


# A Series can store one-dimensional labeled data.
scores = pd.Series(
    [85, 92, 78, 88],
    index=["Amina", "Yusuf", "Hodan", "Ali"],
    name="score",
)

print("Student scores:")
print(scores)

print("\nAmina's score:")
print(scores["Amina"])

print("\nAverage score:")
print(scores.mean())

print("\nHighest score:")
print(scores.max())

print("\nStudents scoring 85 or higher:")
print(scores[scores >= 85])

# Try these yourself:
# 1. Add another student and score.
# 2. Print the lowest score with min().
# 3. Change the filter from >= 85 to >= 90.
