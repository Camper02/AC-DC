def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)

    for next in [i for i in graph[start] if i not in visited]:
        dfs(graph, next, visited)

    return visited


with open("input.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

graph = {}
inverted_graph = {}
n = len(data)
for i in range(n):
    r = []
    for j in range(n):
        if data[i][j] == "1":
            r.append(j)
    graph[i] = r

for i in range(n):
    inverted_graph[i] = []

for i in range(n):
    for j in range(n):
        if data[i][j] == "1":
            inverted_graph[j].append(i)

n = len(graph)

i_p = []
for i in range(n):
    new = sorted(dfs(inverted_graph, i))
    if new not in i_p:
        i_p.append(new)

p = []
for i in range(n):
    new = sorted(dfs(graph, i))
    if new not in p:
        p.append(new)



with open("output.txt", "w") as f:
    for i in range(len(p)):
        f.write("{}: {}\n".format(i, p[i]))