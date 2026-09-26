# 04_calculator.py
# Level 1 — Topic 4: Functions, *args, **kwargs, lambdas

def calculate(operation, *args, **kwargs):
    """Flexible calculator supporting multiple numbers and options."""
    if not args:
        raise ValueError("At least one number required")

    precision = kwargs.get("precision", 2)
    verbose = kwargs.get("verbose", False)

    if operation == "add":
        result = sum(args)
    elif operation == "multiply":
        result = 1
        for num in args:
            result *= num
    elif operation == "average":
        result = sum(args) / len(args)
    else:
        raise ValueError(f"Unknown operation: {operation}")

    result = round(result, precision)

    if verbose:
        print(f"Operation: {operation} | Numbers: {args} → Result: {result}")

    return result


# Lambda examples
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0


if __name__ == "__main__":
    print(calculate("add", 10, 20, 30, precision=0, verbose=True))
    print(calculate("multiply", 2, 3, 4, 5))
    print(calculate("average", 85, 90, 78, 92, precision=1))

    print(square(7))
    print(list(filter(is_even, range(10))))
