marks=int(input("Enter students score:"))
if marks>=80 and marks<=100:
    print("You scored an A")
elif marks>=60 and marks<=79:
    print("You scored a B")
elif marks>=40 and marks<=59:
    print("You scored a C")
elif marks>=30 and marks<=39:
    print("You scored a D")
elif marks>=0 and marks<=29:
    print("You have failed")
else:
    print("Wrong input")


#CREATE A PYTHON PROGRAMME TO CHECK IF A GIVEN YEAR IS LEAP
#THE YEAR IS DIVISIBLE BY 4 BUT NOT DIVISIBLE BY 100
#EXCEPTIF IT IS ALSO DIVISIBLE BY 400