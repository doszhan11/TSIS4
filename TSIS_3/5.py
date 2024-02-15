def num_nn(b):
    for num in range(0, b + 1):
        yield num

a = int(input("B:"))

for s in num_nn(a):
    print(s)
