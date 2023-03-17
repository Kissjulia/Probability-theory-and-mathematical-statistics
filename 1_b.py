# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
from math import factorial
import numpy as np


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


n = combinations(52, 4)
print(f'n = {n}')
m = sum([combinations(4, 1)*combinations(48, 3), combinations(4, 2) * combinations(48, 2), combinations(4, 3) * combinations(48, 1), 1])
print(f'm = {m}')
p = m / n
print(p)
# Ответ: 28%