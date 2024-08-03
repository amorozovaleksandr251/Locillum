# Assuming you have a list of tuples representing operations
data_source = [
    ('ADD', 'item1'),
    ('REM', 'item2'),
    ('MOD', 'item3'),
    ('GET', 'item4'),
    ('SET', 'item5')
]

# Filter out ADD, REM, and MOD tuples
filtered_data = [tuple for tuple in data_source if tuple[0] not in ['ADD', 'REM', 'MOD']]

print(filtered_data)
