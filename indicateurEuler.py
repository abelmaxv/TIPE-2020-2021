from crible_eratosthene import eratosthene
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

def phi(n):
    """Indicateur d'Euler"""
    L = eratosthene(n)
    c = 1
    for i in range(len(L)):
        if n%L[i] ==0:
            c*=(1-1/L[i])
    return n*c 

N = np.array(list(range(10000)))
P = [phi(n) for n in N]
plt.scatter(N,P, s=0.5)
plt.title("Indicateur d'Euler")
plt.show()
