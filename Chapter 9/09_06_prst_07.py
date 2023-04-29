content=True
i=1
with open("log.txt") as f:
    while content:
        
        content= f.readline()
    
        if 'python' in content:
            print(content)
            print(f"Ye, python is present on the line {i}")
        i+=1