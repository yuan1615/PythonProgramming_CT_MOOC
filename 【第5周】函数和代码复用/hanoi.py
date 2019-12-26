# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 14:24:44 2019

@author: Xin
"""

count = 0

def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)
hanoi(5, "A", "B", "C")
print(count)


def prime(m):
    for i in range(2, m):
        if m%i == 0:
            return False
    return True

n = eval(input())

count = 0
while count < 5:
    if prime(n) and count < 4:
        print(n, ",", end = "")
        count += 1
    n += 1
