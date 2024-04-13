from numba import jit, njit, types, vectorize
import time
import numpy as np

test_list = np.arange(100000)


@vectorize(nopython=True)
def non_list_function(item):
    if item % 2 == 0:
        return 2
    else:
        return 1

# t1 = time.perf_counter()
# test_1 = non_list_function(20)
# print(test_1)
# t2 = time.perf_counter()
# print("time 1: ", t2 - t1)
#
# t3 = time.perf_counter()
# test_2 = non_list_function(test_list)[0:5]
# print(test_2)
# t4 = time.perf_counter()
# print("time 2: ", t4 - t3)
#
# t5 = time.perf_counter()
# test_3 = non_list_function(test_list)[0:5]
# print(test_3)
# t6 = time.perf_counter()
# print("time 3: ", t6 - t5)




@njit
def allocated_func(input_list):
    output_list = np.zeros_like(input_list)
    for ii, item in enumerate(input_list):
        if item % 2 == 0:
            output_list[ii] = 2
        else:
            output_list[ii] = 1
    return output_list


t7 = time.perf_counter()
test_4 = allocated_func(test_list)
t8 = time.perf_counter()
print("time 4: ", t8 - t7)

t9 = time.perf_counter()
test_5 = allocated_func(test_list)
t10 = time.perf_counter()
print("time 5: ", t10 - t9)





