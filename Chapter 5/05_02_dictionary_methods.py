my_dict={
    "fast": "in a quick manner",
    "tuhin": "a coder",
    "marks":[23, 56, 99],
    "another_dict":{"tuhin": "player"},
    1:2
}
print(my_dict.keys())
print(my_dict.values())
print(my_dict)
update_dict={"lovish": "friends"}   #updates the dictionary withadding somke key-value pairs from the update dict.
my_dict.update(update_dict)
print(my_dict)
update_dict={"lovish": "friends",
              "tuhin":"a dancer"}
my_dict.update(update_dict)
print(my_dict)

print(my_dict.get("tuhin"))  #print value associated with key "tuhin"
print(my_dict["tuhin"])      #print value associated with key "tuhin"

#The difference
print(my_dict.get("tuhin2"))    #returns none as tuhin2 is not present in the dictionary.
print(my_dict["tuhin2"])    #tyhrow a error as tuhin2 is not present in the dictionary.

