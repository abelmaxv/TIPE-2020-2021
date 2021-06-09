import math
from crible_eratosthene import eratosthene
import numpy as np
import matplotlib.pyplot as plt


def pol_to_cart(n):
    return n * np.cos(n), n * np.sin(n)

def create_plot(nums, figsize=8, s=None):
    nums = np.array(list(nums))
    x, y = pol_to_cart(nums)
    plt.figure(figsize=(figsize, figsize))
    plt.scatter(x, y, s=s)
    plt.title("Spirale des nombres premiers")
    plt.show()

primes = eratosthene(10**5)
create_plot(primes, s=0.15)