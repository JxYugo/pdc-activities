
continue_calculation = True
result = 0

def addition(number, result):
    return result + number
    
def subtraction(number, result):
    return result - number

# Put multiplication 

# Put division function here

print("Enter +, -, *, or / to start operating.")
print("Enter 'q' to quit.")
print("Enter 'c' to clear result")

while continue_calculation:

    print (f"\nCurrent result: {result}")
    op = input("Enter operation: ")

    if op == 'q':
        continue_calculation = False

    elif op == 'c':
        result = 0
        print("Result cleared")

    elif op in {"+", "-", "*", "/"}:

        try:
            num = float(input("Enter Number: "))

            if op == '+':
                result = addition(num, result)
            
            elif op == '-':
                result = subtraction(num, result)

            # Put multiplication elif here

            # Put division elif here

        except ValueError:
            print("Invalid Number")

    else:
        print("Invalid Operation")

print("Calculator Closed")