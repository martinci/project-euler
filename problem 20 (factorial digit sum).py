def factorial(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial(n-1)

s=str(factorial(100))
suma=0
for c in s:
	suma+=int(c)
print(suma)
