print("Enter Num 1:")
num1 = input()
print("Enter Num 2:")
num2 = input()

try:
    int(num1) + int(num2)
except Exception as e:
    print(e)

print("This line is very important")   
