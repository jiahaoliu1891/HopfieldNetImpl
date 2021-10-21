# http://web.cs.ucla.edu/~rosen/161/notes/hopfield.html
# Demo Hopfield Network

# patterns
cat = [0,1,1,0,1]
dog = [1,0,1,0,1]
# 5 neurons
N = 5
# Compute the weight Matrix
W = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(i, N):
        if i == j:
            W[i][j] = 0
        else:
            for V in [cat, dog]:
                W[i][j] += (2*V[i] - 1)*(2*V[j] - 1)
            W[j][i] = W[i][j]

print(W)





