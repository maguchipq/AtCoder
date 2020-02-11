N,C = [int(zz) for zz in input().split()]
S = [int(zz) for zz in input().split()]

l = 0
r = N-1
while r > l:
    if S[l]+S[r] == C:
        print('Yes')
        exit()
    elif S[l]+S[r] > C:
        r -= 1
    else:
        l += 1

print('No')
