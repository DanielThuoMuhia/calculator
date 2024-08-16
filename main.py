from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = { 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
             }


def calculator():
    print(logo)
    num_1 = float(input("Whats the first number?: "))

    for symbol, value in operations.items():
        print(symbol)

    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num_2 = float(input("Whats the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function (num_1, num_2)

        print(f"{num_1} {operations_symbol} {num_2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ") == "y":
            num_1 = answer
        else:
            should_continue = False  
            calculator()  

calculator()