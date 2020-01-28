N = int(input())
A = [[int(zz),i+1] for i,zz in enumerate(input().split())]
A.sort()

[print(i[1],end=' ') for i in A]
