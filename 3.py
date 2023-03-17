# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали. Какова вероятность того, что все извлеченные детали окрашены?
from math import factorial
import numpy as np


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combinations(9, 3)
print(m)

n = combinations(15, 3)
print(n)

p = m / n
print(f'С вероятностью {p * 100}% все извлеченные детали окрашены')