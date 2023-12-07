def findMax(a, b):
    """
    Finds the maximum of two values.

    Parameters:
    - a (int or float): The first value.
    - b (int or float): The second value.

    Returns:
    - int or float: The maximum value.
    """
    if a > b:
        max_value = a
    else:
        max_value = b
    return max_value


result1 = findMax(5, 10)
result2 = findMax(-3, 0)
result3 = findMax(7.5, 3.8)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
