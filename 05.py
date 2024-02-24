x = [4, -2, -7, 6, 3, 1]


n = len(x)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if abs(x[j]) > abs(x[j + 1]):
            x[j], x[j + 1] = x[j + 1], x[j]

print(x)
