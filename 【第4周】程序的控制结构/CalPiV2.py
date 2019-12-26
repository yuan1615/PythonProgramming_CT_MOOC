# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 09:54:48 2019

@author: Xin
"""

from random import random
from time import perf_counter

DARTS = 1000 * 1000
hits = 0
start = perf_counter()
for i in range(1, 1 + DARTS):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits += 1
pi = 4 * (hits/DARTS)

print("圆周率的值是：{:.6f}".format(pi))
print("运行时间是：{:.4f}s".format(perf_counter()-start))














