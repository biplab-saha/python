# prime and not prime Check
def is_prime(num):
    if num <= 1 :
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True

num = int(input("Enter The Number: "))
print(is_prime(num))
        