
n = int(input("Num: "))

even = [str(num) for num in range(0, n + 1, 2)]

result = ', '.join(even)

print(result)
