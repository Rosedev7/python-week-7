import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
try:
    data = pd.read_csv("iris.csv")  # Replace 'iris.csv' with your dataset's name
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Dataset not found! Please check the file name and path.")

# Display the first few rows
print(data.head())

# Check the structure of the dataset
print(data.info())

# Check for missing values
print("Missing values:\n", data.isnull().sum())

# Clean the dataset (drop or fill missing values if any)
data = data.dropna()  # Dropping missing values (if any)
print("Dataset after cleaning:\n", data.head())

# Basic statistics
print("Basic Statistics:\n", data.describe())

# Grouping: Example - Average petal length by species
group_stats = data.groupby('variety')['petal.length'].mean()
print("Average petal length by species:\n", group_stats)

# Line chart (example: time-series data placeholder)
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['petal.length'], label="Petal Length")
plt.title("Trend of Petal Length")
plt.xlabel("Index")
plt.ylabel("Petal Length")
plt.legend()
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
group_stats.plot(kind='bar', color='skyblue')
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length")
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['sepal.length'], bins=10, color='lightgreen', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data['sepal.length'], data['petal.length'], color='purple', alpha=0.7)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# Observations:
# 1. The histogram shows that most sepal lengths are between 5 and 7.
# 2. The scatter plot indicates a positive correlation between sepal length and petal length.
# 3. The bar chart shows significant differences in petal length across species.

