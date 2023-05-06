a = 9
def func():
    global a
    a = 8
    print(f"The initial value of a is {a}")
    a = 900
    print(f"Now the value of a is {a}")
    
print(f"Let's see the value of a is {a}")
func()
print(a)  # after declaring the global keyword, the value of the a became 900... without it the value will be 9.