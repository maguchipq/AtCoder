# C問題

一見こうしようと誰もが思うはずである…

```python
N = int(input())
A = [int(zz) for zz in input().split()]

[print(A.index(i+1)+1, end=' ') for i in range(N)]
```

indexはO(N)かかるのでどう考えてもこれではO(N^2)でアウト  
なぜ気づかなかったんだ俺；；

というわけでこれ

```python
N = int(input())
A = [[int(zz),i+1] for i,zz in enumerate(input().split())]
A.sort()

[print(i[1],end=' ') for i in A]
```

sortはリストの最初の値を参照してsortしてくれるので後はやるだけ  
こんな感じの手法は結構使う…もっといい方法があるかもしれないが

# D問題

解説AC

確かによく考えればgcd(A,B)の値xを素因数に1を足したものが答えになる…

gcdを使うときはAtCoderでは  
```python
from fractions import gcd
```
としよう
