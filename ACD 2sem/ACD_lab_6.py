with open("inputt.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

n = len(data)
edges = []
for i in range(n):
    r = []
    for j in range(n):
        if data[i][j] != "0":
            edges.append([int(data[i][j]), i, j])

edges.sort(key=lambda x: x[0])
res = []
for i in edges:
    l, start, end = i
    f_s, f_e = False, False
    for j in res:
        if start in j[1::]:
            f_s = True
        if end in j[1::]:
            f_e = True
    if f_s and f_e:
        pass
    else:
        res.append(i)

print(res)