A,B,X = [int(zz) for zz in input().split()]

def calc_cost(i):
    return A*i+B*(len(str(i)))

def check_buy(i):
    if calc_cost(i) <= X:
        return True
    else:
        return False

l = 0
r = 10**9

if check_buy(r):
    print(r)
    exit()

while True:
    m = (l+r)//2
    if check_buy(m):
        l = m+1
    else:
        r = m-1

    if r <= l:
        if l == 0:
            print(0)
        elif check_buy(l):
            print(l)
        elif check_buy(l+1):
            print(l+1)
        else:
            print(l-1)
        exit()
