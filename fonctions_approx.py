from crible_eratosthene import eratosthene
import numpy as np
import matplotlib.pyplot as plt

def pi(n):
    """La fonciton qui compte les nombres premiers"""
    L = eratosthene(n)
    return len(L)


th_nb_prem = lambda n : n/np.log(n)  # x-> x/(log x), l'approximation fournie par le théorème des nomrbes premiers 

def Li(x, n = 10**4):
   
    """On utilise la méthode des rectangles à gauche pour approximer l'intégrale
    de 2 à x de dt/ln(t) """
    
    f = lambda t : 1/np.log(t)
    h = (x-2)/n
    s = 0 
    t = 2
    for k in range(n):
        s+=f(t)
        t+=h
    return h*s



N = np.array(list(range(2,1000)))
P = np.array([pi(n) for n in N ])
A = th_nb_prem(N)
L= np.array([Li(n) for n in N])
plt.plot(N,P, label='pi(x)')
plt.plot(N,A, label = 'x/log(x)')
plt.plot(N,L,label= 'Li(x)')
plt.legend()
plt.title("Comparaison des approximations de pi(x)")

plt.show()
