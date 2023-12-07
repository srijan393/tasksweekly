to_seconds = lambda hours, minutes: hours * 3600 + minutes * 60

result1 = to_seconds(1, 30)
result2 = to_seconds(2, 45)
result3 = to_seconds(0, 15)

print("Result 1:", result1, "seconds")
print("Result 2:", result2, "seconds")
print("Result 3:", result3, "seconds")