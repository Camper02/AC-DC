def dijkstra(u, n, G, weights):
    d = [float('inf')] * n
    used = [False] * n
    d[u] = 0
    for i in range(n):
        v = None
        for j in range(n):
            if not used[j] and (v is None or d[j] < d[v]):
                v = j
        if d[v] == float('inf'):
            break
        used[v] = True
        for e in G[v]:
            if d[v] + weights[v][e] < d[e]:
                d[e] = d[v] + weights[v][e]
    return d


def main():
    n = int(input())
    G = [[] for _ in range(n)]
    weights = []
    for i in range(n):
        row = list(map(int, input().split(' ')))
        for j in range(n):
            if row[j] != 0:
                G[i].append(j)
        weights.append(row)
    dist = dijkstra(0, n, G, weights)
    print(dist)


main()