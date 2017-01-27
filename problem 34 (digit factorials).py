def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

fac=[factorial(n) for n in range(0,10)]

def is_curious(n):
	suma=0
	for d in str(n):
		suma+=fac[int(d)]
	if suma==n:
		return True
	return False

# If the number n has k digits, the sum of its factorials is at most k*(9!) and n is at least 10**(k-1).
# This means that we must have k*(9!) <= 10**(k-1), where we obtain k<=8.
print(sum([n for n in range(3,8*factorial(9)) if is_curious(n)]))
