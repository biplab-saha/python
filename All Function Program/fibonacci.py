def fibo(n):
    l =[]
    a,b=0,1
    for _ in range(n):
        l.append(a)
        a,b =b,a+b
    return l 
print(fibo(10))
  