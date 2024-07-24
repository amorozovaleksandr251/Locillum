import pandas as pd

# Sample DataFrame
data = {
    'PRID': [1, 2, 2, 3, 4, 4, 5],
    'Value': ['A', 'B', 'B', 'C', 'D', 'D', 'E']
}
df = pd.DataFrame(data)

# Removing duplicates based on the 'PRID' column and resetting the index
df = df.drop_duplicates(subset=['PRID']).reset_index(drop=True)

print(df)
