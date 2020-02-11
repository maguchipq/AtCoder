from itertools import accumulate

N,K = [int(zz) for zz in input().split()]
A = [int(zz) for zz in input().split()]

A.sort()
li = list(accumulate(A))

ans = 0
for i in range(N-K+1):
    ans += li[-1]-li[i]-(N-K+1-i)*A[i]

print(ans)
