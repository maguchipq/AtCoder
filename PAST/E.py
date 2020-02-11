from copy import deepcopy

N,Q = [int(zz) for zz in input().split()]

li = [[0]*N for _ in range(N)]
for _ in range(Q):
    command = [int(zz) for zz in input().split()]
    li2 = deepcopy(li)
    if command[0] == 1:
        li2[command[1]-1][command[2]-1] = 1
    elif command[0] == 2:
        for j in range(N):
            if li[j][command[1]-1] == 1:
                li2[command[1]-1][j] = 1
    else:
        for j in range(N):
            if li[command[1]-1][j] == 1:
                for k in range(N):
                    if li[j][k] == 1:
                        li2[command[1]-1][k] = 1
    li = deepcopy(li2)

for i in range(N):
    li[i][i] = 0

# print(np.array(li))
for i in range(N):
    ans = ''
    for j in range(N):
        if li[i][j] == 0:
            ans += 'N'
        else:
            ans += 'Y'
    print(ans)
