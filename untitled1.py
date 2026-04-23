import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Task 1: First few records ---")
df = pd.read_csv('sample_data.csv')
print(df.head())

mean_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
min_marks = df['Marks'].min()
std_marks = df['Marks'].std()

print("\n--- Task 2: Data Analysis ---")
print(f"Mean Marks: {mean_marks:.2f}")
print(f"Max Marks: {max_marks}")
print(f"Min Marks: {min_marks}")
print(f"Standard Deviation of Marks: {std_marks:.2f}")

plt.figure(figsize=(10, 6))
plt.plot(df['Name'], df['Marks'], marker='o', linestyle='-', color='b')
plt.title('Line Plot: Name vs Marks')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df_sorted = df.sort_values('Marks', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Name', y='Marks', data=df_sorted, palette='viridis')
plt.title('Bar Chart: Name vs Marks')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(df['Marks'], bins=5, kde=True, color='purple')
plt.title('Histogram: Marks Distribution')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Marks', data=df, s=100, color='orange')
plt.title('Scatter Plot: Age vs Marks')
plt.xlabel('Age')
plt.ylabel('Marks')
plt.tight_layout()
plt.show()

numeric_df = df[['Age', 'Marks']]
plt.figure(figsize=(6, 4))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Heatmap: Correlation Matrix')
plt.tight_layout()
plt.show()

pairplot = sns.pairplot(df[['Age', 'Marks', 'Department']], hue='Department', palette='Set2')
pairplot.fig.suptitle('Pair Plot: Relationships', y=1.02)
plt.show()

