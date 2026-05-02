import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# n = 1000
# user_id = np.random.randint(1, 100, n)
# age = np.random.randint(18, 60, n)
# products = ["phone", "laptop", "tablet", "watch"]
# product = np.random.choice(products, n)
# revenue = np.random.randint(10, 500, n)
# rating = np.random.uniform(1, 5, n)
#
# df = pd.DataFrame({
#     "user_id": user_id,
#     "age": age,
#     "product": product,
#     "revenue": revenue,
#     "rating": rating})
#
# df.loc[np.random.choice(df.index, 10), "rating"] = np.nan
#
# df.to_csv("ecommerce.csv", index=False)
# print(df.head())

df = pd.read_csv("ecommerce.csv")
# print("Размер датасета: ",df.shape)
# print("Типы данных: ",df.info())
# print("Пропуски: ",df.isnull().sum())
# print("Статистика: ",df.describe())

median_rating = df["rating"].median()
df["rating"] = df["rating"].fillna(median_rating)

# print(df["revenue"].describe())

print("Общая выручка: ",df["revenue"].sum())
print("Средний чек: ",df["revenue"].mean())
print("Медиана: ",df["revenue"].median())
print("Количество заказов: ",len(df))
print("Уникальных пользователей: ",df["user_id"].nunique())

top_users = df.groupby("user_id")["revenue"].sum().sort_values(ascending=False).head(10)
print(top_users)

repeat = df["user_id"].value_counts()
print(len(repeat[repeat > 1]))

age_revenue_mean = df.groupby("age")["revenue"].mean()
print(age_revenue_mean)

