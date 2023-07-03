def Majina(fname,lname,age):
    print("My name is "+ fname+" "+lname+" and Im ",age," years old")



Majina("Ronny","Mutuma",22)
Majina("Brian","Kimathi",24)
Majina("Victor","Munene",23)
#create a function that calcs the average of a list



def Calculate_average(numbers):
    total=sum(numbers)
    count=len(numbers)
    average=total/count
    return average


data=[4,6,4,7,2,8,9,5,3,1]
answer=Calculate_average(data)
print("The average is:",answer)

#create a function to display a palindrome
#create a function to find the longest string in alist of item


