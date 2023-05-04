from primes import primes_vanilla, primes_optimized
from time import perf_counter

num = 5000
s1 = perf_counter()
f = primes_vanilla(num)
e1 = perf_counter()
print(f[-10:])
print(e1 - s1)

s2 = perf_counter()
s = primes_optimized(num)
e2 = perf_counter()
print(s[-10:])
print(e2 - s2)
