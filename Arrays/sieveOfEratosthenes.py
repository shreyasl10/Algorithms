def Primes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p*p <= n):
        if prime[p] is True:
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    for i in range(2, n+1):
        if prime[i] is True:
            print(i)


n = int(input())
Primes(n)
