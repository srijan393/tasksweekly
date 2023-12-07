def multiply_values(a, b=None):
    """
    Multiply two numeric values together.

    Parameters:
    - a (int or float): The first numeric value.
    - b (int or float, optional): The second numeric value. If not provided, 'a' is multiplied by itself.

    Returns:
    - int or float: The result of the multiplication.
    """
    if b is None:
        result = a * a
    else:
        result = a * b
    return result

result1 = multiply_values(5, 3)
result2 = multiply_values(7)
result3 = multiply_values(2.5, 4.0)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
