import sys

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

if __name__ == "__main__":
    _, operation, x, y = sys.argv
    x, y = int(x), int(y)
    if operation == 'add': print(add(x,y))
    elif operation == 'subtract': print(subtract(x,y))
    elif operation == 'multiply': print(multiply(x,y))
    elif operation == 'divide': print(divide(x,y))
    else: print("Invalid operation")