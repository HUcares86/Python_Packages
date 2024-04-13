import random
import time
from numba import jit


@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    print(4.0 * acc / nsamples)
    return 4.0 * acc / nsamples


def monte_carlo_pi_no_numba(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    print(4.0 * acc / nsamples)
    return 4.0 * acc / nsamples

t1 = time.perf_counter()
monte_carlo_pi_no_numba(1000000)
t2 = time.perf_counter()
print("time 1: ", t2 - t1)

t3 = time.perf_counter()
monte_carlo_pi(1000000)
t4 = time.perf_counter()
print("time 2: ", t4 - t3)

t5 = time.perf_counter()
monte_carlo_pi(1000000)
t6 = time.perf_counter()
print("time 3: ", t6 - t5)




