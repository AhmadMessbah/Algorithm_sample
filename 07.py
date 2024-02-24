names = ["mohsen", "ali", "reza"]
phones = [245, 456, 123]

n = len(names)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if names[j] > names[j + 1]:
            names[j], names[j + 1] = names[j + 1], names[j]
            phones[j], phones[j + 1] = phones[j + 1], phones[j]

for i in range(3):
    print(names[i], phones[i])
