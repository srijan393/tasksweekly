def multiply_values(a, b=None):
    if b is None:
        result = a * a
    else:
        result = a * b
    return result
result1 = multiply_values(a=6, b=4)
result2 = multiply_values(b=8, a=8)
result3 = multiply_values(a=1.5, b=3.5)

# Display the returned values
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
