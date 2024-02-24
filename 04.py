x = ["b","Z","M","a"]

n = len(x)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if x[j].lower() > x[j + 1].lower():
            x[j], x[j + 1] = x[j + 1], x[j]

print(x)
