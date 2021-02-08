def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter The number: "))

print("factorial using Recursive Method", factorial_recursive(number))    