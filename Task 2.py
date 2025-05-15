import pandas as pd

df = pd.read_csv('task2 dset.csv')

print("Initial Info:")
print(df.info())

df = df.drop_duplicates()

print("\nMissing Values:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].median())

df['Gender'] = df['Gender'].str.strip().str.capitalize()

print("\nCleaned Data Preview:")
print(df.head())


#Distribution 0f ages
import matplotlib.pyplot as plt

plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#Gender
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', color=['purple', 'orange'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

#Age
import seaborn as sns

sns.boxplot(x='Gender', y='Age', data=df)
plt.title('Age Distribution by Gender')
plt.show()
