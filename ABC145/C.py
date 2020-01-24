from math import factorial

N = int(input())
li = [[int(zz) for zz in input().split()] for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i+1,N):
        ans += ((li[i][0]-li[j][0])**2+(li[i][1]-li[j][1])**2)**(1/2)

print(ans*2/N)
