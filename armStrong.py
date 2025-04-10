num = int(input("Enter a number: "))  
sum = 0  
temp = num  
num_digits = len(str(num))  # Count number of digits

while temp > 0:
    digit = temp % 10  
    sum += digit ** num_digits  # Add digit^num_digits to sum
    temp //= 10  

# Condition statement to check Armstrong number
if num == sum:
    print(f"an Armstrong number is {num}.")
else:
    print(f"{num} is not an Armstrong number.")

print("Given A Number Value Is:",sum)
    
