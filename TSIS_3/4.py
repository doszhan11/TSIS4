def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("B:"))
b = int(input("A:"))

for square in squares(a, b):
    print(square)
