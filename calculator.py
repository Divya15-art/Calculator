# Program make a simple calculator

# This function add two numbers def add(x,y):
def add(x,y):
    return x + y

# This function subtracts two numbers def subtract(x,y):
def subtract(x,y):
    return x - y

# This function multiply two numbers def multiply(x,y):
def multiply(x,y):
    return x * y

# This function divide two numbers def divide(x,y):
def divide(x,y):
    return x / y

num1 = int(input("Enter Number1 :"))
num2 = int(input("Enter Number2 :"))

print("Sum :", add(num1, num2))
print("Difference :", subtract(num1, num2))
print("Product :", multiply(num1, num2))
print("Quotient :", divide(num1, num2))
