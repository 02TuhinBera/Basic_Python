from functools import reduce

# Demostration for Map
square = lambda x: x*x
l = [1, 2, 3, 4, 5]
c = map(square, l)
print(list(c))

# Demostration for Filter
greater = lambda x: x>8
l = [5, 96, 78, 2, 56, 4, 32, 1]
d = filter(greater, l)
print(list(d))

# Demostration for Reduce
sum = lambda x, y: x+y
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = reduce(sum, l)
print(d)