def divisibl(n):
    for num in range(0, n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Num:"))

divisible_n = divisibl(n)

for num in divisible_n:
    print(num)
