to_seconds = lambda hours, minutes=0: hours * 3600 + minutes * 60

result1 = to_seconds(1)  #
result2 = to_seconds(2)

print("Result 1:", result1, "seconds")
print("Result 2:", result2, "seconds")