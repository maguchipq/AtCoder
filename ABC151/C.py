N,M = [int(zz) for zz in input().split()]

li = [[0,0] for _ in range(N)]

for i in range(M):
    p,s = [zz for zz in input().split()]
    if li[int(p)-1][1] == 0 and s == 'WA':
        li[int(p)-1][0] += 1
    elif s == 'AC':
        li[int(p)-1][1] = 1

penalty = 0
AC_count = 0
for i in range(N):
    penalty += li[i][0]*li[i][1]
    AC_count += li[i][1]

print(AC_count,penalty)
