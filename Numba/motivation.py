from IPython.display import Image
from numba import jit, njit, types, vectorize
import time
import numpy as np
import matplotlib.pyplot as plt

# Let's mix wet friction with dry friction, this makes the behavior
# of the system dependent on the initial condition, something
# may be interesting to study by running an exhaustive simluation

# def friction_fn(v, vt):
#     if v > vt:
#         return - v * 3
#     else:
#         return - vt * 3 * np.sign(v)
#
#
# def simulate_spring_mass_funky_damper(x0, T=10, dt=0.0001, vt=1.0):
#     times = np.arange(0, T, dt)
#     positions = np.zeros_like(times)
#
#     v = 0
#     a = 0
#     x = x0
#     positions[0] = x0 / x0
#
#     for ii in range(len(times)):
#         if ii == 0:
#             continue
#         t = times[ii]
#         a = friction_fn(v, vt) - 100 * x
#         v = v + a * dt
#         x = x + v * dt
#         positions[ii] = x / x0
#     return times, positions
#
# plt.plot(*simulate_spring_mass_funky_damper(0.1))
# plt.plot(*simulate_spring_mass_funky_damper(1))
# plt.plot(*simulate_spring_mass_funky_damper(10))
# plt.legend(['0.1', '1', '10'])
# plt.show()
#
# t1 = time.perf_counter()
# test_1 = simulate_spring_mass_funky_damper(0.1)
# t2 = time.perf_counter()
# print("time 1: ", t2 - t1)

"--------------------------------------------------------------------------------------------------------------------"

@njit(nogil=True)
def friction_fn(v, vt):
    if v > vt:
        return - v * 3
    else:
        return - vt * 3 * np.sign(v)


@njit(nogil=True)
def simulate_spring_mass_funky_damper(x0, T=10, dt=0.0001, vt=1.0):
    times = np.arange(0, T, dt)
    positions = np.zeros_like(times)

    v = 0
    a = 0
    x = x0
    positions[0] = x0 / x0

    for ii in range(len(times)):
        if ii == 0:
            continue
        t = times[ii]
        a = friction_fn(v, vt) - 100 * x
        v = v + a * dt
        x = x + v * dt
        positions[ii] = x / x0
    return times, positions


plt.plot(*simulate_spring_mass_funky_damper(0.1))
plt.plot(*simulate_spring_mass_funky_damper(1))
plt.plot(*simulate_spring_mass_funky_damper(10))
plt.legend(['0.1', '1', '10'])
plt.show()

t1 = time.perf_counter()
test_1 = simulate_spring_mass_funky_damper(0.1)
t2 = time.perf_counter()
print("time 1: ", t2 - t1)

t1 = time.perf_counter()
test_2 = simulate_spring_mass_funky_damper(0.1)
t2 = time.perf_counter()
print("time 2: ", t2 - t1)



t1 = time.perf_counter()
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(8) as ex:
    ex.map(simulate_spring_mass_funky_damper, np.arange(0, 1000, 0.1))
t2 = time.perf_counter()
print("time 2: ", t2 - t1)