class Sample:
    a = "Harry"

obj = Sample()
obj.a = "vikky"
# Sample.a = "Vikky"   --> it will help to change the class otherwise it will never change class

print(Sample.a)
print(obj.a)