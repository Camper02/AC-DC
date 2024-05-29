def dfs(v, G, was, comp):
    was[v] = True
    comp.append(v)
    for u in G[v]:
        if not was[u]:
            dfs(u, G, was, comp)


n = int(input())
G = [[] for i in range(n)]
for i in range(n):
    row = list(map(int, input().split(' ')))
    for j in range(n):
        if row[j] == 1:
            G[i].append(j)
was = [False] * n
num_copms = 0
comps = []
for i in range(n):
    if not was[i]:
        num_copms += 1
        comp = []
        dfs(i, G, was, comp)
        comps.append(comp)
print(num_copms, comps)