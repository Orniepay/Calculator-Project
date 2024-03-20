import math

print("")
print("Free Basic Calculator")
print("")

def add(x, y):
    """
    Performs addition of two numbers and prints the result.

    @param x First number
    @param y Second number
    @returns None
    """
    answer = x + y
    print("")
    print("============================")
    print(str(x) + " + " + str(y) + " = " + str(answer) + "\n")

def sub(x, y):
    """
    Performs subtraction of two numbers and prints the result.

    @param x First number
    @param y Second number
    @returns None
    """
    answer = x - y
    print("")
    print("============================")
    print(str(x) + " - " + str(y) + " = " + str(answer) + "\n")

def mul(x, y):
    """
    Performs multiplication of two numbers and prints the result.

    @param x First number
    @param y Second number
    @returns None
    """
    answer = x * y
    print("")
    print("============================")
    print(str(x) + " * " + str(y) + " = " + str(answer) + "\n")

def div(x, y):
    """
    Performs division of two numbers and prints the result.

    @param x Dividend
    @param y Divisor
    @returns None
    """
    answer = x / y
    print("")
    print("============================")
    print(str(x) + " / " + str(y) + " = " + str(answer) + "\n")

def mod(x, y):
    """
    Calculates the modulus of two numbers and prints the result.

    @param x First number
    @param y Second number
    @returns None
    """
    answer = x % y
    print("")
    print("============================")
    print(str(x) + " % " + str(y) + " = " + str(answer) + "\n")

def exp(x, y):
    """
    Calculates the exponentiation of two numbers and prints the result.

    @param x Base number
    @param y Exponent
    @returns None
    """
    answer = x ** y
    print("")
    print("============================")
    print(str(x) + " ** " + str(y) + " = " + str(answer) + "\n")

def flrdiv(x, y):
    """
    Performs floor division of two numbers and prints the result.

    @param x Dividend
    @param y Divisor
    @returns None
    """
    answer = x // y
    print("")
    print("============================")
    print(str(x) + " // " + str(y) + " = " + str(answer) + "\n")

def sqrt(x):
    """
    Calculates the square root of a number and prints the result.

    @param x The number to find the square root of
    @returns None
    """
    answer = math.sqrt(x)
    print("")
    print("============================")
    print(" √ " + " of " + str(x) + " is " + str(answer) + "\n")

def fact(x):
    """
    Calculates the factorial of a number and prints the result.

    @param x The number to find the factorial of
    @returns None
    """
    answer = math.factorial(x)
    print("")
    print("============================")
    print(str(x) + "!" + " = " + str(answer) + "\n")

while True:
    """
    Main loop of the calculator. Presents options to the user and processes user input to perform calculations.
    """ 
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor division")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Quit")

    operator = input("Choose your operator above: (1-10) -> ")
    print("")

    if operator == "1." or operator == "1":
        print("")
        print("Addition")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        add(x, y)
    elif operator == "2." or operator == "2":
        print("")
        print("Subtraction")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        sub(x, y)
    elif operator == "3." or operator == "3":
        print("")
        print("Multiplication")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        mul(x, y)
    elif operator == "4." or operator == "4":
        print("")
        print("Division")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        div(x, y)
    elif operator == "5." or operator == "5":
        print("")
        print("Modulus")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        mod(x, y)
    elif operator == "6." or operator == "6":
        print("")
        print("Exponentiation")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        exp(x, y)
    elif operator == "7." or operator == "7":
        print("")
        print("Floor division")
        print("")
        x = int(input("Input your first number: "))
        print("")
        y = int(input("Input your second number: "))
        flrdiv(x, y)
    elif operator == "8." or operator == "8":
        print("")
        print("Square Root")
        print("")
        x = int(input("Input your number: "))
        sqrt(x)
    elif operator == "9." or operator == "9":
        print("")
        print("Factorial")
        print("")
        x = int(input("Input your number: "))
        fact(x)
    elif operator == "10." or operator == "10":
        print("--Program Ended--")
        print("")
        quit()