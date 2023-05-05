def function():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(a / b)
        return a/b
        
    except Exception as e:
        print(f"This problem occurred: {e}")
        return 0
    
    finally:
        print("I will always be executed")  # but this line will always executed despite being in a function...
        
    # print("I will always be executed")   # if we are return from a fuction, this line will not always executed..

function()