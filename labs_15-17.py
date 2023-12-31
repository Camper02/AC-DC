import re


class TreeNode:
    def __init__(self, value):
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

    # не рекурсивный прямой обход
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

    # линейное представление
    def linear_representation(self):
        result = []
        if self.left:
            result.append(self.left.linear_representation())
        result.append(str(self.value))
        if self.right:
            result.append(self.right.linear_representation())
        return f"({','.join(result)})"

    # поиск значения
    def search(self, value):
        if self.value == value:
            return True
        elif value < self.value and self.left:
            return self.left.search(value)
        elif value > self.value and self.right:
            return self.right.search(value)
        else:
            return False

    # Добавление значения
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    # вывод дерева на дисплей
    def display_graphically(self, level=0, prefix="Корень: "):
        if self is not None:
            print(" " * (level * 4) + prefix + str(self.value))
            if self.left:
                self.left.display_graphically(level + 1, "Л--- ")
            if self.right:
                self.right.display_graphically(level + 1, "П--- ")

    # удаление значения
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Найдена вершина для удаления
            if self.left is None and self.right is None:
                # У вершины нет потомков
                return None
            elif self.left is None:
                # У вершины есть только правый потомок
                return self.right
            elif self.right is None:
                # У вершины есть только левый потомок
                return self.left
            else:
                # У вершины есть оба потомка
                successor = self.right.find_min()
                self.value = successor.value
                self.right = self.right.delete(successor.value)
        return self

def build_tree(values, parent):
    left_child = True
    if not isinstance(parent, TreeNode):
        parent = TreeNode(int(parent))

    if len(values) > 5:
        if "(" in values:
            for i in range(len(values)):
                if "(" == values[i]:
                    start = i
                elif ")" == values[i]:
                    return build_tree(
                        values[:start - 1] + [build_tree(values[start:i + 1], values[start - 1])] + values[i + 1:],
                        parent)

    for i in range(len(values)):
        node = None
        if isinstance(values[i], str):
            if values[i].isdigit():
                node = TreeNode(int(values[i]))
        elif isinstance(values[i], TreeNode):
            node = values[i]
        elif values[i] == ',':
            left_child = False
            continue

        if values[i] == "(" or values[i] == ")":
            continue
        if left_child:
            parent.left = node
            left_child = False
        else:
            parent.right = node

    return parent

# пояснялка ниже
def build_tree_from_string(string):
    values = re.findall(r'\d+|-\d+|\(|\)|,', string)
    values = [val for val in values if val != '']
    return build_tree(values[1:], TreeNode(int(values[0])))

input_string = input("Введите бинарное дерево в линейно-скобочной записи: ")
Tree = build_tree_from_string(input_string)
Tree.display_graphically()

while True:
    print("1-Добавить значение\n2-Удалить значени\n3-Найти значение\n"
          "4-Прямой обход\n5-Центральный обход \n6-Концевой обход\n"
          "7-Не рекурсивный прямой обход\n0-Выход")

    command = input("Введите команду:")
    if command == "0":
        break
    if command == "1":
        value = input("Введите значние: ")
        Tree.insert(int(value))
    elif command == "2":
        value = input("Введите значние: ")
        Tree.delete(int(value))
    elif command == "3":
        value = input("Введите значние: ")
        print("Значение существует в дереве" if Tree.search(int(value)) else "Значения не существует в дереве")
    elif command == "4":
        Tree.pre_order(Tree)
    elif command == "5":
        Tree.in_order(Tree)
    elif command == "6":
        Tree.post_order(Tree)
    elif command == "7":
        Tree.non_recursive_pre_order(Tree)
    else:
        print("Неизвестная команда")
    print("--------------------------")
Tree.display_graphically()

# Строка из задания для проверки
# 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))

# def build_tree_from_string(string): - Это объявление функции build_tree_from_string, которая принимает один аргумент string, который является строкой, представляющей структуру дерева.

# values = re.findall(r'\d+|-\d+|\(|\)|,', string) - Здесь используется регулярное выражение для поиска в строке string следующих сущностей:

# \d+ - Положительные целые числа.
# -\d+ - Отрицательные целые числа.
# \( - Открывающие скобки.
# \) - Закрывающие скобки.
# , - Запятые.
# Результат поиска сохраняется в переменной values в виде списка строк.

# values = [val for val in values if val != ''] - Эта строка удаляет пустые строки (пустые символы), если такие имеются в списке values. Оставшиеся значения сохраняются в той же переменной values.

# return build_tree(values[1:], TreeNode(int(values[0]))) - Возвращается результат вызова функции build_tree с двумя аргументами:

# values[1:] - Это список значений values с удаленным первым элементом. Он предполагается, что это остаток строки после первого найденного числа или символа.
# TreeNode(int(values[0])) - Здесь первый элемент списка values (первое найденное число) преобразуется в целое число и передается как аргумент для создания нового объекта TreeNode.
