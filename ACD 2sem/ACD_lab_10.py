def find_euler_cycle(adj_matrix):
    n = len(adj_matrix)
    stack = [0]
    cycle = []

    while stack:
        v = stack[-1]
        found_next = False

        for i in range(n):
            if adj_matrix[v][i] > 0:
                adj_matrix[v][i] -= 1
                adj_matrix[i][v] -= 1
                stack.append(i)
                found_next = True
                break

        if not found_next:
            cycle.append(stack.pop())

    return cycle[::-1]


with open("inputt.txt", "r") as f:
    data = f.read()
data = [i.split(" ") for i in data.split("\n")]

n = len(data)
for i in range(n):
    for j in range(n):
        data[i][j] = int(data[i][j])

euler_cycle = find_euler_cycle(data)

if euler_cycle:
    print("Euler cycle found:")
    print(euler_cycle)
else:
    print("No Euler cycle found")