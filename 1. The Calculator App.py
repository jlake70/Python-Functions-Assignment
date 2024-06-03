#Task 1

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return print("Change the value for 'b', cannot divide by zero.")
    else: 
        return a / b

print(addition(3, 6))
print(subtraction(5, 4))
print(multiplication(3, 6))
print(division(20, 5))


# Task 2 and Task 3

def user_input():
    a = int(input("What is your first value?: "))
    b = int(input("What is your second value?: "))
    operation = input("What operation do you need?: (+, -, *, /) ")

    if operation == "+":
        print(addition(a, b))    
    elif operation == "-":
        print(subtraction(a, b))
    elif operation == "*":
        print(multiplication(a, b))
    elif operation == "/":
        print(division(a, b))
    else:
        print("Invalid choice, please revise entry.")


user_input()
