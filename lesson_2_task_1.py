<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

print(df.head())
print(df.describe())

filtered = df[(df["rating"] > 8) & (df["year"]>2010)]
print(filtered)

df_sort = df.sort_values("year")

plt.plot(df_sort["year"], df_sort["rating"])
plt.xlabel("Год")
plt.ylabel("Рейтинг")
plt.title("Рейтинг фильмов по годам")
plt.show()

plt.scatter(df["year"], df["rating"])
plt.xlabel("Год")
plt.ylabel("Рейтинг")
plt.title("Год vs Рейтинг (scatter)")
plt.show()

plt.hist(df["rating"], bins=7)

plt.xlabel("Рейтинг")
plt.ylabel("Количество фильмов")
plt.title("Распределение рейтингов фильмов")

plt.grid(True)
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movies.csv")

print(df.head())
print(df.describe())

filtered = df[(df["rating"] > 8) & (df["year"]>2010)]
print(filtered)

df_sort = df.sort_values("year")

plt.plot(df_sort["year"], df_sort["rating"])
plt.xlabel("Год")
plt.ylabel("Рейтинг")
plt.title("Рейтинг фильмов по годам")
plt.show()

plt.scatter(df["year"], df["rating"])
plt.xlabel("Год")
plt.ylabel("Рейтинг")
plt.title("Год vs Рейтинг (scatter)")
plt.show()

plt.hist(df["rating"], bins=7)

plt.xlabel("Рейтинг")
plt.ylabel("Количество фильмов")
plt.title("Распределение рейтингов фильмов")

plt.grid(True)
plt.show()
>>>>>>> 176a36c76dc1f55746efcdec79a5eda7136b24d9
