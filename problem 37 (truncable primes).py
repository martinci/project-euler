from is_prime import is_prime
	
primes={}
trunc=[]
for n in range(2,10**6):
	if is_prime(n):
		primes[str(n)]=False
for p in primes.keys():
	br=0
	for l in range(1,len(p)):
		if not p[l:] in primes.keys():
			br=1
			break
		if not p[:l] in primes.keys():
			br=1
			break
	if br==0 and int(p)>7:
		primes[p]=True
		
print(sum([int(p) for p in primes.keys() if primes[p]]))
