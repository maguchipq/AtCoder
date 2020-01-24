X,Y = [int(zz) for zz in input().split()]

mod = 10**9+7
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

a = (2*Y-X)/3
b = (2*X-Y)/3

if a != int(a):
    print(0)
    exit()

a = int(a)
b = int(b)
N = a+b

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = cmb(N,a,mod)%(10**9+7)
print(int(ans))
