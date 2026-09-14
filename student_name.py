import pandas as pd

# Create the DataFrame
data = {
    "Student Name": ["Amit", "Priya", "Rahul", "Sneha", "Arjun"],
    "Roll Number": [101, 102, 103, 104, 105],
    "Marks": [85, 78, 92, 75, 88],
    "Attendance": [90, 85, 95, 80, 92]
}

df = pd.DataFrame(data)

# Filter students who scored above 80 marks
filtered_df = df[df["Marks"] > 80]

# Display the filtered records
print("Students who scored above 80 marks:")
print(filtered_df)
