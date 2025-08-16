import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)

# Add a new column
df['Senior'] = df['Age'] > 35
print("\nDataFrame with 'Senior' column:")
print(df)
