ma = 0
for n in range(9):
    a = bin(n)[2:]
    if a[-1] == '0':
        a = '10' + a
    else:
        a = '1' + a + '01'
    r = int(a, 2)
    if r > ma:
        ma = r
print(r)