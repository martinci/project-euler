def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if not n%2:
        return False
    if n<9:
        return True
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True

if __name__ == "__main__":
    primes=[]
    for i in range(1,100):
        if is_prime(i):
            primes.append(i)
    print(primes)
