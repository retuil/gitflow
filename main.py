def F(n):
    if n < 3:
        return n + 3
    elif n % 3 == 0:
        return (n + 2) * F(n-4)
    else:
        return n + F(n-1) + 2 * F(n-2)

print(F(20))


def K(n):
    if n == 1:
        return 1
    elif n > 1:
        return 3*K(n-1) + G(n-1) - n + 5


def G(n):
    if n == 1:
        return 1
    elif n > 1:
        return K(n-1) + 3*G(n-1) - 3*n

print(K(14) + G(14))


def N(n):
    if n > 15:
        return n
    else:
        return 2*N(n+1) + 5*n + 2


print(N(2))