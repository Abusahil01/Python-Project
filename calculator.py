def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

try:
    num1=int(input("Enter the number:"))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Please insert the choice (1 - 4):"))
    num2=int(input("Enter the next number:"))

    if choice==1:
        print(num1, "+", num2, "=", add(num1,num2))

    elif choice==2:
        print(num1, "-", num2, "=", sub(num1,num2))

    elif choice==3:
        print(num1, "*", num2, "=", mul(num1,num2))

    elif choice==4:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(num1, "/", num2, "=", div(num1, num2))

    else:
        print("Invalid Input !!!!!!")
        print("Enter number (1/2/3/4):")
except ValueError:
    print("Invalid!!!")