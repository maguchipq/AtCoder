from bisect import bisect_left, bisect_right

N = int(input())
li = [int(zz) for zz in input().split()]

li.sort()

ans = 0
for i in range(N):
    for j in range(i+1,N):
        l = bisect_right(li,li[j]-li[i])
        r = bisect_left(li,li[i]+li[j])
        ans += r-l
        if l <= i < r:
            ans -= 1
        if l <= j < r:
            ans -= 1
print(ans//3)
