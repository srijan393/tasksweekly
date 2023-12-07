def calcAve(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

result1 = calcAve(10, 20, 30)
result2 = calcAve(5, 15)
result3 = calcAve(2, 7, 9, 12, 18)


print("Average 1:", result1)
print("Average 2:", result2)
print("Average 3:", result3)
