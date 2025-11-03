def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
x = int(input("Enter the number you want to find factorial of: "))
result = factorial(x)
print(f"The factorial of {x} is {result}")