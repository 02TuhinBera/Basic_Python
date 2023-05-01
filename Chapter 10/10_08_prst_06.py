class Sample:
    a = "Harry"
    def __init__(slf, name):   # we can change "self" into anyparameter or anyname, it will work anyway. abut for better understanding
        slf.name = name   # we should use "self" as a parameter.....
        
obj = Sample("Tuhin")
print(obj.name)
