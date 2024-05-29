def forBellman(s, n, G, weights):
    d = [float('inf')] * n
    d[s] = 0
    for i in range(n):
        for u in range(n):
            for v in G[u]:
                if d[v] > d[u] + weights[u][v]:
                    d[v] = d[u] + weights[u][v]
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
    dist = forBellman(0, n, G, weights)
    print(dist)


main()