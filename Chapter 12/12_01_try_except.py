try:
    print("Hello World")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
    if b > 199:
        raise Exception("This number is too large")

except ValueError:
    print("Value error occurred")
    
except ZeroDivisionError:
    print("This is zero division error")
    
except Exception as e:
    print(f"This problem occured: {e}")   # Whenever the problem in the try block, then the Exception block will be executed..

else:
    print("Try was successful")
    
print("See for yourself")