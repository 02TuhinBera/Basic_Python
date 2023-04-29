def fahr(cel):
    return (cel*9/5)+32

c=int(input("Enter the celsius value: \n"))
f=fahr(c)
print("The Fahrenheit Tempareture is " + str(f)) 