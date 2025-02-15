import pandas as pd 

df = pd.read_csv("Titanic-Dataset.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.describe())

print(df.isnull().sum())


                            # Extracts Insights :- 
                            # -------- --------



survival_count = df["Survived"].value_counts()
print(survival_count)

gender_count = df["Sex"].value_counts()
print(gender_count)


average_age = df["Age"].mean()
print("Average Age :" , average_age)

pclass_count = df["Pclass"].value_counts()
print(pclass_count)


                               # Data Cleaning :- 
                               # ---- --------


df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].isnull().sum())

df.to_csv("Cleaned_Titanic-Dataset.csv", index = False)
