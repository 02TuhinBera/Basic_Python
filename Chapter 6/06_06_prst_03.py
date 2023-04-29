text = input("Enter the text\n")
if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subcribes this" in text):
    spam = True
elif("click this" in text):
    spam = True
else:
    spam = False
    
if(spam):
        print("This is a spam text")
else:
        print("This is not spam text")