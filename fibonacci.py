number=int (input("Enter the number for fibonacci: "))
def fibonacci(number):
    if number ==0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)# fn = fn-1+ fn-2
for i in range (number):
    print(fibonacci(i))    




    