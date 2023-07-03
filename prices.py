age=int(input("Enter your Age:"))
if age==0 or age<=5:
    print("You can Enter for free")
elif age==6 or age<=12:
    print("Pay Ksh500 as entrance fee")
elif age==13 or age<=17:
    print("Pay Ksh1000 as entrance fee")
elif age>=18:
    print("Pay Ksh1500 as entrance fee")

