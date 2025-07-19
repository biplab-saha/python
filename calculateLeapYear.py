year=int(input("Enter a Year: "))
# Condition
if year%4==0 and year%400==0 or year%100!=0  :
    print(" Leap Year")
else:
    print("Not a Leap Year")    