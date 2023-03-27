n = 2 * 729 ** 1021 - 2 * 243 ** 1022 + 81 ** 1023 - 2 * 27 ** 1024 - 1025
a = ''
while True:
    a = str(n % 3) + a
    n = n // 3
    if n == 0:
        break
a = str(int(a))
print(a.count('0'))
