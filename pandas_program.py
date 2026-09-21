import pandas as pd

marks = pd.Series([78, 85, 92, 66], index=["Amit", "Ravi", "Neha", "Sara"])
print(marks)
print(marks["Neha"])

#####################################################################

import pandas as pd

data = {
    "Name": ["Amit", "Ravi", "Neha", "Sara"],
    "Age": [21, 22, 20, 23],
    "Marks": [78, 85, 92, 66]
}

df = pd.DataFrame(data)
print(df)

######################################################################

# Select one column
print(df["Name"])

# Select multiple columns
print(df[["Name", "Marks"]])

# Select rows using label-based indexing
print(df.loc[0])

# Select rows using integer position
print(df.iloc[0:2])
