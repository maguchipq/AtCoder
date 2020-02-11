S = input()
ans = []

tmp = ''
flag = 0
for i in S:
    if i.isupper():
        if flag == 0:
            tmp += i.lower()
            flag = 1
        else:
            tmp += i.lower()
            ans.append(tmp)
            tmp = ''
            flag = 0
    else:
        tmp += i

ans.sort()
tmp = ''
for i in ans:
    tmp += i[0].upper()+i[1:-1]+i[-1].upper()

print(tmp)
