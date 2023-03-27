def f(x, y, A):
    return (x + y <= 32) or (y <= x + 4) or (y >=A)



for A in range(1, 10 ** 3):
    if all(f(x, y, A) for x in range(1, 1500) for y in range(1, 1500)):
        print(A)
