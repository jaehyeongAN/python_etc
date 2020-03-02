import time
import numba
from numba import jit

def for_python(s, e):
    tot = 0
    for i in range(s, e):
        tot += i
    return tot

# @numba.vectorize
@jit(nopython=True)
def for_numba(s, e):
    tot = 0
    for i in range(s, e):
        tot += i
    return tot

# start = time.time()
# result = for_python(1,100000000)
# print(result)
# end = time.time()
# print(end - start)

start = time.time()
result = for_numba(1,1000000000)
print(result)
end = time.time()
print(end - start)
