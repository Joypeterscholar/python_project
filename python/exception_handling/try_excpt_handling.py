def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return f"input must be a number"


print(multiply("two", "three"))
