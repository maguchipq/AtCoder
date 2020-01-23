N = int(input())
li = [int(zz) for zz in input().split()]

ans = 0
tmp = 10**9
for i in range(N):
    if li[i] < tmp:
        tmp = li[i]
        ans += 1

print(ans)
