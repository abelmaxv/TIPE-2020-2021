from crible_eratosthene import eratosthene
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')


def pol_to_cart(n):
    return n * np.cos(n), n * np.sin(n)

def create_plot(nums, figsize=8, s=None):
    nums = np.array(list(nums))
    x, y = pol_to_cart(nums)
    plt.figure(figsize=(figsize, figsize))
    plt.scatter(x, y, s=s)
    plt.title("Spirale des nombres")
    plt.show()

primes = eratosthene(10**6)
nums = np.array(list(range(10**6)))
create_plot(primes, s= 0.05)