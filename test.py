from collections import deque

N = int(input())

glaph = [[] for _ in range(N)]
w_glaph = [[-1]*N for _ in range(N)]
ans = [0]*N

for _ in range(N-1):
    v,t,w = [int(zz) for zz in input().split()]
    w_glaph[v-1][t-1] = w
    glaph[v-1].append(t-1)
    glaph[t-1].append(v-1)

visited = [0]*N
q = deque([0])
visited[0] = 1
while q:
    now = q.popleft()
    for i in glaph[now]:
        if not visited[i]:
            q.append(i)
            visited[i] = 1
            if w_glaph[now][i]%2 == 0:
                ans[i] = ans[now]
            else:
                ans[i] = ans[now]^1

[print(i) for i in ans]