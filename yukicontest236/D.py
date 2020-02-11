from itertools import accumulate

N = int(input())
A = [int(zz) for zz in input().split()]
A.sort()

llist = list(accumulate(A))
rlist = list(accumulate(A[::-1]))

ans = 0
for i in range(1,N//2):
    ans = max(llist[i+1]+rlist[i]-i*A[i+1],ans)
print(ans)
