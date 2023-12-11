squares = [4, 9, 16, 25, 49, 64, 100]
value= 3
if value in squares:
    squares.remove(value)
    print(f"Value {value} removed.")
else:
    print(f"Value {value} is not present in the list.")
print("Updated squares list:", squares)
