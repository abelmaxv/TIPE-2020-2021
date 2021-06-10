def pgcd(a, b):
    if a<b:
        return pgcd(b,a)
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return pgcd(b,a%b)


def pollards_rho(n):
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = pgcd(abs(x-y), n)
    if d != n: return d

n = 47508355408452438672873207975244607143697401672601919005182981061393486991065174351724507009558369983282837049901
p = pollards_rho(n)
print ('{} = {} * {}'.format(n, p, n/p))