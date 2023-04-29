Name="Tuhin"
print(Name[0])
# print(Name[3])
# print(Name[4])
# Name[3]="f" --> does not work(change)
print(Name[0:5])   #string slicing
print(Name[:4])    #same as print(Name[0:4])
print(Name[1:])    #same as print(Name[1:5])
c=Name[-4:-1]      #same as print(Name[1:4])
print(c)
#Slicing with skip value
Name="TuhinIsGood"
d=Name[0::2]       #same as print(Name[0:10:2]) and here 2 means, when it print the text.... it will the second character.....
print(d)
