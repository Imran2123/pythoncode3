def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def divide(a, b):
    """Return the division of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"{x} - {y} = {subtract(x, y)}")
    try:
        print(f"{x} / {y} = {divide(x, y)}")
    except ValueError as e:
        print(e)
