n = int(input("Enter a number to print its multiplication table in reverse order: "))

# iterate over the range from 10 to 0 in reverse order
for i in range(10, 0, -1):
    # calculate the product of n and i
    product = n * i
    # print the result in a formatted string
    print(f"{n} x {i} = {product}")
