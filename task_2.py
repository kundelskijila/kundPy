
import numpy as np
import matplotlib.pyplot as plt

checks  = np.random.normal(loc=600, scale=300, size=1000)

checks = checks.clip(100,2000)

print("Минимальный чек:", checks.min())
print("Максимальный чек:", checks.max())
print("Среднее значение:", checks.mean())

plt.hist(checks, bins=30)
plt.xlabel("Сумма чека")
plt.ylabel("Количество людей")
plt.title("Распределение чеков в кафе")
plt.show()
