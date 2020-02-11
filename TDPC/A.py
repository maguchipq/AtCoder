N = int(input())
p = [int(zz) for zz in input().split()]

dp = [[0]*(10001) for _ in range(N)]
dp[0][0] = 1
dp[0][p[0]] = 1

for i in range(1,N):
    for j in range(10000-p[i],-p[i]-1,-1):
        dp[i][j+p[i]] = max(dp[i-1][j],dp[i-1][j+p[i]],dp[i][j+p[i]])

print(sum(dp[-1]))
