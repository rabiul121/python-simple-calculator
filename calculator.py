def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}\n")


def subtract(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}\n")


def division(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}\n")


def multiplication(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}\n")


while True:
    print("A. Addition\nB. Subtraction\nC. Division\nD. Multiplication\nE. Exit")

    choice = input("Choose the option: ")
    if choice == 'a' or choice == 'A':
        print("\nAddition\n-----------")
        a = int(input("Enter first number: "))
        b = int(input("Enter Second number: "))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print("\nSubtractions\n-----------")
        a = int(input("Enter first number: "))
        b = int(input("Enter Second number: "))
        subtract(a, b)
    elif choice == 'c' or choice == 'C':
        print("\nDivision\n-----------")
        a = int(input("Enter first number: "))
        b = int(input("Enter Second number: "))
        division(a, b)
    elif choice == 'd' or choice == 'D':
        print("\nMultiplication\n-----------")
        a = int(input("Enter first number: "))
        b = int(input("Enter Second number: "))
        multiplication(a, b)
    elif choice == 'e' or choice == 'E':
        print("Program Closed")
        quit()
    else:
        print("\nWrong Input!")
        print("Enter valid option: ")
