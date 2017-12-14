from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first seem'
    def __repr__(self):
        return f"{self.__class__.__name__}({OrderedDict(self)})"

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


oc = OrderedCounter('abracadabra')

print(oc.__repr__())
print(oc.__reduce__())
