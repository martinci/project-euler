from is_prime import is_prime

s=0
for n in range(2*10**6):
	if is_prime(n):
		s+=n
print(s)
