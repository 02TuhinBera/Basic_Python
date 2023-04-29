# use the open function to read a file 
# f=open("sample.txt", "r")
f=open("sample.txt")  # By default the mode is r
data=f.read()
# data=f.read(5)  # reads first 5 charactes from the file..
print(data)
f.close()