N = int(input())
A = [int(input()) for _ in range(N)]

tmp = A[0]
for i in range(1,N):
    if tmp == A[i]:
        print('stay')
    elif tmp > A[i]:
        print('down {0}'.format(tmp-A[i]))
    else:
        print('up {0}'.format(A[i]-tmp))
    tmp = A[i]
