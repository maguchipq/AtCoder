H,N = [int(zz) for zz in input().split()]
A = [int(zz) for zz in input().split()]

if H > sum(A):
    print('No')
else:
    print('Yes')
