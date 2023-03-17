# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
from math import factorial
import numpy as np


def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

m = 1

n = combinations(100, 2)

p = m / n

print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными равна {p * 100}%')