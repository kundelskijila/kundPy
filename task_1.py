import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

# --- Проверка requests ---
response = requests.get("https://httpbin.org/html")
print("Статус:", response.status_code)

# --- Проверка BeautifulSoup ---
soup = BeautifulSoup(response.text, "html.parser")
print("Заголовок:", soup.find("h1").text)

# --- Проверка numpy ---
data = np.random.normal(loc=600, scale=200, size=1000)
print("Средний чек:", data.mean())

# --- Проверка matplotlib ---
plt.hist(data, bins=30)
plt.xlabel("Сумма чека")
plt.ylabel("Количество людей")
plt.title("Тест графика")
plt.show()