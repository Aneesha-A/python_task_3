def fact(n):
    if n<2:
        return 1
    else:
        return n*(fact(n-1))
a=int(input("Enter the number:"))
result=fact(a)
print(f"Factorial of {a} is: {result}")
