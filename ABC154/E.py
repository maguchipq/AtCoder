from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

M = int(input())
N = list(str(M))
K = int(input())

keta = len(N)
if K == 1:
    ans = 9*(keta-1)+int(N[0])
elif K == 2:
    if keta > 2:
        ans = cmb(keta-1,2)*81+max(0,int(N[0])-1)*9*(keta-1)
        for i in range(1,keta):
            if int(N[i]) != 0:
                ans += 9*(keta-i-1)+int(N[i])
                break
    else:
        ans = 0
        for i in range(11,M+1):
            if '0' not in str(i):
                 ans += 1
else:
    if keta > 3:
        ans = cmb(keta-1,3)*729+(int(N[0])-1)*81*cmb(keta-1,2)+max(0,int(N[1])-1)*(keta-2)*9
        for i in range(1,keta):
            if int(N[i]) != 0:
                ans += cmb(keta-i-1,2)*81+int(N[i+1])
                for j in range(i,keta):
                    if int(N[j]) != 0:
                        ans += 9*(keta-j-2)
                        break
                break
    else:
        ans = 0
        for i in range(111,M+1):
            if '0' not in str(i):
                ans += 1

print(int(ans))
