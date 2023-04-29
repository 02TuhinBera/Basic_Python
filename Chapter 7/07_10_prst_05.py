# Get input from user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
i = 1

# Calculate sum of first n natural numbers using while loop
while i <= n:
    sum += i
    i += 1

# Display the result
print("The sum of the first", n, "natural numbers is:", sum)
