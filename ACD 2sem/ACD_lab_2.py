from queue import Queue

n = int(input())
G = [[] for i in range(n)]
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] == 1:
            G[i].append(j)
u = int(input())
q = Queue()
q.put(u)
dist = [float('inf')] * n
dist[u] = 0
while not q.empty():
    i = q.get()
    for j in G[i]:
        if dist[j] == float('inf'):
            dist[j] = dist[i] + 1
            q.put(j)
print(dist)

'''
ex input & output:
3
0 1 2
3 0 2
1 2 0
0
[0, 1, inf]
'''