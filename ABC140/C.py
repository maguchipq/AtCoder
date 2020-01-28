N = int(input())
B = [int(zz) for zz in input().split()]

A = [0]*(N)
A[0] = B[0]
A[-1] = B[-1]

for i in range(N-2):
    A[i+1] = min(B[i],B[i+1])

print(sum(A))
