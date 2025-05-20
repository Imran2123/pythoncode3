def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    x = 8
    y = 3
    print(f"{x} - {y} = {subtract(x, y)}")
    try:
        print(f"{x} / {y} = {divide(x, y)}")
    except ValueError as e:
        print(e)
