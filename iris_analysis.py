import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("iris.csv")

print("Shape:", df.shape)
print("Columns:", df.columns)
print(df.head())
print(df.info())
print(df.describe())

sns.pairplot(df, hue="species")
plt.show()

df.hist(figsize=(10, 8), bins=20)
plt.show()

sns.boxplot(data=df)
plt.show()


