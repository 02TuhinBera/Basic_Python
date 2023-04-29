def sum_of_naturals(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_naturals(n-1)

n = int(input("Enter a positive integer: "))
print("The sum of the first", n, "natural numbers is", sum_of_naturals(n))
