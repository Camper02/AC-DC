from random import choice


with open("inputt.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

n = len(data)
edges = []
for i in range(n):
    r = []
    for j in range(n):
        if data[i][j] != "0" and [int(data[i][j]), j, i] not in edges:
            edges.append([int(data[i][j]), i, j])
edges.sort(key=lambda x: x[0])

p = choice(range(n))
res = [min(list(filter(lambda x: p in x[1::], edges)), key=lambda x: x[0])]
edges.remove(res[-1])

for i in res:
    l, start, end = i
    m = 100
    p = []
    for j in edges:
        if start in j[1::] or end in j[1::]:
            if m > j[0]:
                m = j[0]
                p = j
    if m != 100:
        res.append(p)
        edges.remove(res[-1])

print(res)