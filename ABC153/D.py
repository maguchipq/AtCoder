import numpy as np

H = int(input())

x = int(np.log2(H))+1
print(2**x-1)
