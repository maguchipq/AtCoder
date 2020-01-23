N = int(input())
li = [int(zz) for zz in input().split()]

count = 1
ans = 0
ind = 0
while ind < N:
    if li[ind] == count:
        count += 1
        ans += 1
    ind += 1

if ans != 0:
    print(N-ans)
else:
    print(-1)
