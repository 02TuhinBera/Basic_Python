my_dict={
    "pankha": "fan",
    "vastu": "item",
    "manab":"human"
}
print("Option are: ", my_dict.keys())
a=input("Enter you Hindi Word: ")
print("The meaning of your word is : ", my_dict.get(a))   # To avoid error