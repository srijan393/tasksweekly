import math
roots = {n: math.sqrt(n) for n in range(1, 26)}
for num, sqrt_value in roots.items():
    print(f"The square root of {num} is {sqrt_value}")