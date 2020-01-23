import numpy as np

X = int(input())

def checkprime(N):
    for i in range(2,int(np.sqrt(N))+1):
        if N%i == 0:
            return False
    return True

while True:
    if checkprime(X):
        print(X)
        exit()
    X += 1
