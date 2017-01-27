from is_prime import is_prime
from itertools import permutations

digits=[str(i) for i in range(1,10)]

max_pan_prime = 1

for n in range(2,10):
    for permutation in permutations(digits[:n],n):
        temp = "".join(permutation)
        num=int(temp)
        if num>=max_pan_prime and is_prime(num):
            max_pan_prime=num
                    
print(max_pan_prime)
