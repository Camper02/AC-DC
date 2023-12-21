class Hash_func:
    def __init__(self, inp):
        self.lst = []
        for i in range(10):
            self.lst.append([])
        for i in range(len(inp)):
            ind = hash(inp[i])
            self.lst[abs(ind) % 10].append("{}: {} ".format(ind, inp[i]))

    def hash_table(self):
        return self.lst



with open("input.txt", "r") as f:
    hash_ = Hash_func(f.read().split(" "))

table = hash_.hash_table()
with open("output.txt", "w") as f:
    for i in table:
        for j in range(len(i)):
            f.write(i[j])
        f.write("\n")
