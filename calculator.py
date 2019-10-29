# Input definitions

def Calc():
    print("Enter num")
    num1 = input("Enter first number\n")
    num1 = int(num1)
    op = input("Enter operation (+, -, /, ^, * or x)\n")
    num3 = input("Enter second number\n")
    num3 = int(num3)
        
    # Calculations    
    
    if op == "-":                 # Subtraction
        both = num1-num3
    if op == "+":                 # Addition
        both = num1+num3
    if op == "*" or "x":          # Multiplication
        both = num1*num3
    if op == "/":                 # Division
        if num1 > 0 and num3 > 0:
            both = num1/num3
        else:
            print ("Cannot divide by zero")
            exit()
    if op == "^":                 # Powers
        both = num1**num3

    # Output
    output = both    
    print("Your anwser is " + str(output))
