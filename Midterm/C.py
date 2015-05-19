N = int(input())
G = []
G.append(0)#0
G.append(0)#1
G.append(0)#2
G.append(1)#3
for i in range(4, N + 1) :
    G.append(G[i - 1] + G[i - 2] + G[i - 3] + G[i - 4])

print(G[N])
