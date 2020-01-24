# C問題

素数判定はO(N**(1/2))  
制約を見るとN<=10**12

うわあああああああぴったりだあああああああああ

はい，約数を調べてマンハッタン距離が一番短くなるやつを使えばいい

## tips:様々な距離

### マンハッタン距離
L1ノルムとか言われてる

```python
import numpy as np
from numpy import linalg as LA

A = np.array([x1,y1])
B = np.array([x2,y2])

L1norm = LA.norm(A-B,1)
```

で，計算できます！便利！

### ユークリッド距離
L2ノルム

```python
import numpy as np
from numpy import linalg as LA

A = np.array([x1,y1])
B = np.array([x2,y2])

L1norm = LA.norm(A-B,2)
```
