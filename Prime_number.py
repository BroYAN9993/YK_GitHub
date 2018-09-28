#!/usr/bin/env python
# -*- coding:utf-8

def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    pri = {
        2 : True,
    }
    for i in range(3, n):
        pri[i] = False
    for i in range(3, n, 2):
        pri[i] = True
    for i in range(3, n, 2):
        if pri[i]:
            time = 3
            while i * time < n:
                pri[i * time] = False
                time += 1
    count = 0
    for key in pri:
        if pri[key]:
            count += 1
    return count 



print countPrimes(10)
