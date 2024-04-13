from numba import jit, njit, types, vectorize
import time

# test_list = list(range(100000))


def original_function(input_list):
    output_list = []
    for item in input_list:
        if item % 2 == 0:
            output_list.append(2)
        else:
            output_list.append('1')
    return output_list


# t1 = time.perf_counter()
# test_1 = original_function(test_list)[0:10]
# print(test_1)
# t2 = time.perf_counter()
# print("time 1: ", t2 - t1)
#
# jitted_function = jit()(original_function)
# t3 = time.perf_counter()
# test_2 = jitted_function(test_list)[0:10]
# t4 = time.perf_counter()
# print("time 2: ", t4 - t3)
#
# jitted_function = jit()(original_function)
# t5 = time.perf_counter()
# test_3 = jitted_function(test_list)[0:10]
# t6 = time.perf_counter()
# print("time 3: ", t6 - t5)


"-----------------------------------------------------------------------------------"
import numpy as np
test_list = np.arange(100000)


def sane_function(input_list):
    output_list = []
    for item in input_list:
        if item % 2 == 0:
            output_list.append(2)
        else:
            output_list.append(1)
    return output_list


t1 = time.perf_counter()
test_1 = sane_function(test_list)[0:5]
print(test_1)
t2 = time.perf_counter()
print("time 1: ", t2 - t1)

njitted_sane_function = njit()(sane_function)
t3 = time.perf_counter()
test_2 = njitted_sane_function(test_list)[0:5]
t4 = time.perf_counter()
print("time 2: ", t4 - t3)

t5 = time.perf_counter()
test_3 = njitted_sane_function(test_list)[0:5]
t6 = time.perf_counter()
print("time 3: ", t6 - t5)
