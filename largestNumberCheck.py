numOne=int(input("enter the first numbers: "))
numSecond=int(input("enter the second numbers: "))
numThird=int(input("enter the third numbers: "))
if (numOne>numSecond and numOne>numThird):
    print(f"{numOne} largest value..")
elif(numSecond>numOne and numSecond>numThird):
    print(f"{numSecond} laregst value... ")
else:
    print(f"{numThird} largest value..")        
    