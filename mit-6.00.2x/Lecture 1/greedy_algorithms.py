class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result


def value(item):
    return item.get_value()


def weight_inverse(item):
    return 1.0 / item.get_weight()


def density(item):
    return item.get_value() / item.get_weight()


def greedy(items, max_weight, key_function):
    """Assumes items a list, max_weight >= 0,
    key_function maps elements of items to numbers"""
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return result, total_value


def build_items():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    items = []
    for i in range(len(values)):
        items.append(Item(names[i], values[i], weights[i]))
    return items


def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print('Total value of items taken is', val)
    for item in taken:
        print('   ', item)


def test_greedys(max_weight=20):
    items = build_items()
    print('Use greedy by value to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, value)
    print('\nUse greedy by weight to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, weight_inverse)
    print('\nUse greedy by density to fill knapsack of size', max_weight)
    test_greedy(items, max_weight, density)


test_greedys()
