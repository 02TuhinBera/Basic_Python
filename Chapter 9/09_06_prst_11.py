import os

oldname="sample2.txt"
newname="remove_by_python.txt"
with open(oldname, "r") as f:
    content=f.read()

with open(newname, "w") as f:
    f.write(content)
    
os.remove(oldname)