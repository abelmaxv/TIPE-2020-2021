from math import isqrt
import time
import numpy as np

#Crible d'Eratosthène

def temps (f, n):
    """Permet de calculer le temps d'execution d'une fonction f
    avec une entrée n"""
    a = time.time()
    f(n)
    return time.time()-a


def eratosthene(n):
    """Implémentation du crible d'Eratosthène"""
    if n < 2:
        return []
    is_prime = [True]*n
    is_prime[0],is_prime[1] = False, False
    
    for i in range(2, isqrt(n)):
        if is_prime[i]:
            for x in range(i**2, n, i):
                is_prime[x]= False
    
    return np.array([i for i in range(n) if is_prime[i]])

    