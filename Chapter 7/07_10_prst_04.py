num=int(input("Enter the number: \n"))
prime=True
for i in range(2, num):
    if(num%i==0):
        prime=False
        break

if prime:
    print("The number is prime\n")
else:
    print("The number is not prime\n")