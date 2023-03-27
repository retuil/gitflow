from functools import lru_cache
from sys import setrecursionlimit


def m(n):
    return n + 1, n + 4, n * 2


@lru_cache(None)
def f(n):
    if n >= 351:
        return 'win'
    if any(f(x) == 'win' for x in m(n)):
        return 'p1'
    if all(f(x) == 'p1' for x in m(n)):
        return 'w1'
    if any(f(x) == 'w1' for x in m(n)):
        return 'p2'
    if all(f(x) == 'p1' or f(x) == 'p2' for x in m(n)):
        return 'w2'


setrecursionlimit(10**9)
for i in range(1, 351):
    print(i, f(i))