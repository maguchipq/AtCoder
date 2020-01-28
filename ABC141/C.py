N,K,Q = [int(zz) for zz in input().split()]

li = [0]*N
for _ in range(Q):
    A = int(input())
    li[A-1] += 1

for i in range(N):
    if li[i]+K <= Q:
        print('No')
    else:
        print('Yes')
