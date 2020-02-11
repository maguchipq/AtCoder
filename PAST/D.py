N = int(input())
li = [int(input()) for _ in range(N)]
li.sort()

p = [0]*N
for i in range(N):
    p[li[i]-1] += 1

if p.count(1) == N:
    print('Correct')
else:
    print(p.index(2)+1,p.index(0)+1)
