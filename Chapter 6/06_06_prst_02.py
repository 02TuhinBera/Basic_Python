sub1=int(input("Enter the marks of the subject 1: \n"))
sub2=int(input("Enter the marks of the subject 2: \n"))
sub3=int(input("Enter the marks of the subject 3: \n"))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less 33% one of the subject\n")
elif((sub1+sub2+sub3)/3<40):
    print("You are fail because your total percentage is less than 40\n")
else:
    print("You are passed! Congratulations!")
