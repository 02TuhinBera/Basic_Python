a = [0, 2, 5, 9, 'mango']
# i = 0
# for item in a:
#     i = i + 1
#     print(f"Item number {i} is {item}") 
    
    # Another way to do this.....

for i, item in enumerate(a):
    print(f"Item number {i+1} is {item}")    # to start the index number from 1, for this we can do just {i+1}