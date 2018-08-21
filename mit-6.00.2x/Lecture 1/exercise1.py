class Item(object):
    def __init__(self, weight, value, name):
        self.weight = weight
        self.value = value
        self.name = name

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value


def metric1(item):
    try:
        return item.get_value() / item.get_weight()
    except ZeroDivisionError:
        return 0


dirt = Item(4, 0, 'dirt')
computer = Item(10, 30, 'computer')
fork = Item(5, 1, 'fork')
problem_set = Item(0, -10, 'problem_set')

items = [dirt, computer, fork, problem_set]

metrics1 = []
for i in items:
    metrics1.append((i.name, metric1(i)))

print(metrics1)
