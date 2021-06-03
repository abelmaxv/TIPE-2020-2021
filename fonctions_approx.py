from crible_eratosthene import eratosthene
import numpy as np
import matplotlib.pyplot as plt

def pi(n):
    """La fonciton qui compte les nombres premiers"""
    L = eratosthene(n)
    R =[]
    ie = 0
    c = 0
    for i in range(n):
        if ie<len(L) and L[ie]==i: c+=1; ie +=1
        R.append(c)
    return R

approx = lambda n : [0]+[i/np.log(i) for i in range(1,n)]


N = list(range(1000))
P = pi(1000)
A = approx(1000)
plt.plot(N,P)
plt.plot(N,A)

plt.show()
