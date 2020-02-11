S,T = [zz for zz in input().split()]
A,B = [int(zz) for zz in input().split()]
U = input()

if U == S:
    A -= 1
elif U == T:
    B -= 1

print(A,B)
