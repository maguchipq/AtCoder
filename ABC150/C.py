from itertools import permutations

N = int(input())
P = tuple([int(zz)-1 for zz in input().split()])
Q = tuple([int(zz)-1 for zz in input().split()])

li = list(permutations(range(N)))
print(abs(li.index(P)-li.index(Q)))
