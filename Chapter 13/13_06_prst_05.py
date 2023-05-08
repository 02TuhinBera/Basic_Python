from functools import reduce

def max(m, n):
    if m>n:
        return m
    return n

a = [11, 96, 7, 555, 635, 87, 96, 784, 1111]
maxNum = reduce(max, a)
print(maxNum)