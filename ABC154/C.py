N = int(input())
A = [int(zz) for zz in input().split()]

B = len(set(A))
if N == B:
    print('YES')
else:
    print('NO')
