# lab15
# Рекурсивные обходы (прямой, центральный, концевой)
# lab16
# Не рекурсивный прямой обход

class Tree:
    def __init__(self, value, up=None):
        self.up = up
        self.value = value
        self.left = None
        self.right = None

    # прямой обход
    def pre_order(self, node):
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    # центральный обход
    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    # концевой обход
    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    def non_recursive_pre_order(self, node):
        if node:
            stack = [node]
            while stack:
                curroot = stack.pop()
                print(curroot.value)  # Посещение узла
                if curroot.right:
                    stack.append(curroot.right)
                if curroot.left:
                    stack.append(curroot.left)




def creation(char, node, q):
    i = 0
    # print("------")
    # if node:
    #     node.pre_order(node)
    # print(char)
    # print("-----")
    if char[i] == "(":
        i += 1
        if char[i] == ",":
            return creation(char[i:], node, q)
        if char[i].isdigit():
            s = char[i]
            j = i + 1
            while char[j].isdigit():
                s += char[j]
                j += 1
            s = int(s)
            node.left = Tree(s, node)
            if char[j] == "(":
                return creation(char[j:], node.left, q)
            return creation(char[j:], node, q)
    if char[i] == ",":
        i += 1
        if char[i] == ")":
            return creation(char[i:], node.up, q)
        if char[i].isdigit():
            s = char[i]
            j = i + 1
            while char[j].isdigit():
                s += char[j]
                j += 1
            s = int(s)
            node.right = Tree(s, node)
            # print("char - " + char)
            if char[j] == "(":
                # print("chshdfnkjfke")
                return creation(char[j:], node.right, q)
            return creation(char[j:], node, q)
    if char[i] == ")" and len(char) == 1:
        # print("---04rlfroff")
        return q
    if char[i] == ")":
        i += 1
        return creation(char[i:], node.up, q)


# tree = Tree(1)
# tree.left = Tree(2)
# tree.right = Tree(3)
# tree.left.left = Tree(4)
# tree.left.right = Tree(5)

a = input("Введите строку: ")
q = int(a[:a.find("(")])
tree = Tree(q)
a = a[a.find("("):].replace(" ", "")
tree = creation(a, tree, tree)
print("recursive method:")
tree.pre_order(tree)
print("nonrecursive method")
tree.non_recursive_pre_order(tree)
# Строка из задания для проверки
# 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))

# 8
# 3
# 1
# 6
# 4
# 7
# 10
# 14
# 13
