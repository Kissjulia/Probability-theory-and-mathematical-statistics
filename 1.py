# Из колоды в 52 карты извлекаются случайным образом 4 карты. a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial
import numpy as np

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = combinations(13, 4)
print(m)
n = combinations(52, 4)
print(n)
probability = m / n
print(probability)
# Ответ: 0,26%
