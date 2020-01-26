H,N = [int(zz) for zz in input().split()]
li = [[int(zz) for zz in input().split()] for _ in range(N)]

dp = [[0]*(H+1) for _ in range(N)]

for j in range(1,H+1):
    if j <= li[0][0]:
        dp[0][j] = li[0][1]
    else:
        dp[0][j] = dp[0][j-li[0][0]]+li[0][1]

for i in range(1,N):
    for j in range(1,H+1):
        if j <= li[i][0]:
            dp[i][j] = min(li[i][1],dp[i-1][j])
        else:
            dp[i][j] = min(dp[i][j-li[i][0]]+li[i][1],dp[i-1][j])

print(dp[-1][-1])
