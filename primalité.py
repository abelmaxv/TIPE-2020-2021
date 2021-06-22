import random
from RSA import expo_rap

def fermat (n,k):
    """Applique le test de primalité de Fermat k fois à un entier n"""
    premier = True
    for i in range(k):
        a = random.randrange(2,n-1)
        if expo_rap(a,n-1,n) != 1:
            premier = False
    return premier


def miller_rabin(n, k):
    """Applique le test de primalité de Miller Rabin k fois à un entier n"""
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = expo_rap(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = expo_rap(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True