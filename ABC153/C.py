N,K = [int(zz) for zz in input().split()]
H = [int(zz) for zz in input().split()]

H.sort(reverse=True)
print(sum(H[K:]))
