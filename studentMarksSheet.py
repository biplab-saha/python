bengali=int(input("Enter the bengali subject Numbers: "))
english=int(input("Enter the english subject Numbers: "))
math = int (input("Enter the math subject Numbers: "))
algorithm=int(input("Enter the algorithm subject Numbers: "))
totalMarks=(bengali+english+math+algorithm)
marks=float(totalMarks)/4
print(totalMarks)

if (marks>=75):
    print("Distinction....")
elif( marks >=60 and marks <75 ):
    print("Second Divistion...") 
elif( marks >=50 and marks<60 ):
    print("thrid divistion...")
elif ( marks>=40 and marks<50 ):
    print("Student is Fail...")
else:
    print("Rad Card..")              