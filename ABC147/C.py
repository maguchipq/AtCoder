N = int(input())
prefix = '0{}b'.format(N)
li = [[-1]*N for _ in range(N)]

for i in range(N):
    A = int(input())
    for _ in range(A):
        x,y = [int(zz) for zz in input().split()]
        li[i][x-1] = y

ans = 0
for i in range(2**N):
    bin = format(i,prefix)
    flag = 1
    for j in range(N):
        if (i>>j)&1:
            for k in range(N):
                if li[j][k] == 1:
                    if bin[-k-1] != '1':
                        flag = 0
                elif li[j][k] == 0:
                    if bin[-k-1] != '0':
                        flag = 0
    if flag:
        ans = max(ans,list(bin).count('1'))

print(ans)
