N = int(input())
S = input()

ans = 0
tmp = ''
for i in S:
    if tmp != i:
        ans += 1
    tmp = i

print(ans)
