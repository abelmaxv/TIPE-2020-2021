def floyd(f,a):
    """Algorithme de Floyd qui renvoie un couple (i,2i) tel que x_i = x_2i = x
    avec (x_n) la suite def par x_0= a et x_(n+1) = f(x_n) """
    i,x,y=1,f(a),f(f(a))
    while x != y:
        i,x,y= i+1, f(x),f(f(y))
    return i,2*i


def pgcd(a, b):
    """Calcul de PGCD(a,b) via l'algorithme d'euclide"""
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
    else: print('Echec')

n= 2**128 +1
p = pollards_rho(n)
print ('{} = {} * {}'.format(n, p, n/p))
