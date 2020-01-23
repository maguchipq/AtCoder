from fractions import gcd

A,B = [int(zz) for zz in input().split()]

def lcm(a,b):
    return a*b//gcd(a,b)

print(lcm(A,B))
