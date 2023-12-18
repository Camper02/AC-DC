class Hash_func:
    def __init__(self, inp):
        self.lst = []

        for i in range(len(inp)):
            ind = 0
            for j in inp[i]:
                ind += ord(j)
            ind = ind % 1000
            while ind >= len(self.lst):
                self.lst.append("\n")
            while self.lst[ind] != '\n' and len(self.lst) < ind:
                ind += 1
            print(ind)
            self.lst[ind] = "{}: {}\n".format(ind, inp[i])

    def hash_table(self):
        return self.lst



with open("input.txt", "r") as f:
    hash_ = Hash_func(f.read().split(" "))

table = hash_.hash_table()
with open("output.txt", "w") as f:
    for i in table:
        f.write(i)
