x = [4, 2, 3, 1, -7, -9, 200, 590, 200]

print(x)

n = len(x)

for i in range(n - 1):  # دورها
    for j in range(n - 1 - i):  # مقایسه ها
        print(f"{x[j]} > {x[j + 1]}", end=" ")
        if x[j] > x[j + 1]:  # یک عدد از بعدی بزرگتر
            x[j], x[j + 1] = x[j + 1], x[j]  # swap جابجایی
        print(x)
    print("-----------------")

print(x)
