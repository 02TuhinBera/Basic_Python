b=set()
print(type(b))
print(b)

#Adding values
b.add(4)
b.add(5)
b.add(5)                 #Adding a value repeatedly does not change the set
b.add((4, 5, 6))          #We can not add a list in a set but we can add a tuple in a set
    #b.add({4:5})        #We also can not  add a dictionary in a set 
print(b)

print(len(b))            #print the length of the set 

b.remove(5)              #Remove 5 from the set
print(b)

print(b.pop())
print(b)

b.clear()               #It will clear the set and make a empty set.
print(b)


