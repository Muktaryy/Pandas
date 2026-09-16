"""Practice for lesson 01: pandas basics.

Run this file, inspect the output, and then change the sample data yourself.
"""

import pandas as pd


students = {
    "name": ["Amina", "Ali", "Hodan"],
    "score": [85, 78, 92],
}

df = pd.DataFrame(students)

print(df)
