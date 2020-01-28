from fractions import gcd

A,B = [int(zz) for zz in input().split()]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

x = gcd(A,B)

print(len(set(prime_factorize(x)))+1)
