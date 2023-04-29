def remove_and_strip(string, word):
    newStr=string.replace(word, "")
    return newStr.strip()

this="  Harry is a boy   "
n=remove_and_strip(this, "Harry")
print(n)