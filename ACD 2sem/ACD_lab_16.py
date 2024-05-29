from collections import namedtuple

Item = namedtuple('Item', 'value weight')
items = Item(4, 5), Item(3, 4), Item(3, 2), Item(2, 1)
capacity = 6


def best_value(nitems, weight_limit):
    if nitems == 0:
        return 0
    elif items[nitems - 1].weight > weight_limit:
        return best_value(nitems - 1, weight_limit)
    else:
        return max(best_value(nitems - 1, weight_limit),
            best_value(nitems - 1, weight_limit - items[nitems - 1].weight) + items[nitems - 1].value)


result = []
weight_limit = capacity
for i in reversed(range(len(items))):
    if best_value(i + 1, weight_limit) > best_value(i, weight_limit):
        result.append(items[i])
        weight_limit -= items[i].weight

print(result)