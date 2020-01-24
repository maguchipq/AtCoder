import numpy as np
from numpy import linalg as LA

N = int(input())
li = [[1,N]]

for i in range(2,int(np.sqrt(N))+1):
    if N%i == 0:
        li.append([i,N//i])

ans = 10**12
for i in li:
    x,y = i
    tmp = LA.norm([x-1,y-1],1)
    if ans > tmp:
        ans = tmp

print(ans)
