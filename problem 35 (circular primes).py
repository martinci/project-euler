from is_prime import is_prime
	
c_primes={}
for i in range(10**6):
	if is_prime(i):
		c_primes[i]=True
for k in c_primes.keys():
	s=str(k)
	for i in range(len(s)):
		if not int(s[i:]+s[:i]) in c_primes.keys():
			c_primes[k]=False
			break
			
print(len([n for n in c_primes.keys() if c_primes[n]]))
