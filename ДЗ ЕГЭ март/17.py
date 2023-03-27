f = [int(i) for i in open('файлы/17_6752.txt', 'r').readlines()]
k = 0
kp = 0
ms = -10000000
for i in f:
    if i % 3 == 0:
        k += 1

for i in range(len(f) - 1):
    a, b = f[i], f[i + 1]
    if (a < 0 or b < 0) and a + b < k:
        kp += 1
        if a + b > ms:
            ms = a + b
print(kp, ms)