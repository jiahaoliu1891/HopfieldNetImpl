from math import sqrt
import numpy as np
# http://web.cs.ucla.edu/~rosen/161/notes/hopfield.html
# Demo Hopfield Network

# patterns
cat = [0,1,1,0,1]
dog = [1,0,0,0,1]
# 5 neurons
N = 5
# Compute the weight Matrix
def train(N, patterns):
    W = [[0 for _ in range(N)] for _ in range(N)]
    W = np.array(W)
    for i in range(N):
        for j in range(i, N):
            if i == j:
                W[i][j] = 0
            else:
                for V in patterns:
                    W[i][j] += (2*V[i] - 1)*(2*V[j] - 1)
                W[j][i] = W[i][j]
    W = W / len(patterns)
    return W

W = train(N, [cat, dog])
import random



def retreive(N, pattern, W):
    ans = np.array(pattern)
    # random pick a node and Asynchronous update
    for k in range(4):
        seq = list(range(N))
        random.shuffle(seq)
        for i in seq:
            s_i = (W[i] * ans).sum()
            if s_i >= 0:
                ans[i] = 1
            else:
                ans[i] = 0
    return ans
print('----little cat----')
little_cat = np.array([0,1,0,0,1])
print(retreive(N,little_cat,W))
print('----little dog----')
little_dog = np.array([0,0,0,0,0])
print(retreive(N,little_dog,W))