from math import isqrt

#Crible d'Eratosthène

def eratosthene(n):
    if n <= 2:
        return []
    is_prime = [True]*n
    is_prime[0],is_prime[1] = False, False
    
    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i**2, n, i):
                is_prime[x]= False
    return [i for i in range(n) if is_prime[i]]
    