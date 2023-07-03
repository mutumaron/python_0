year=int(input("Enter the year:"))
if year%4 ==0 and (year%100 !=0 or year%400 ==0):
    print("Its a leap year")
else:
    print("This is not a leap year")


#write a python progg to calc the ticket price of a movie theater according to age
#0-5 free
#6-12 500
#13-17 1000
#18+ 1500