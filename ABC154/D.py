from itertools import accumulate

N,K = [int(zz) for zz in input().split()]
P = [int(zz) for zz in input().split()]

Q = [0] + list(accumulate(P))
ans = 0
for i in range(N-K+1):
    ans = max(ans,Q[i+K]-Q[i])

print((ans+K)/2)
