from ColoredShape import Root, ColoredShape


class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print('Drawing at position:', self.x, self.y)


class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.moveable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.moveable.draw()
        super().draw()


class MoveableColoredShape(ColoredShape, MoveableAdapter):
    pass


MoveableColoredShape(color='red', shapename='triangle', x=10, y=20).draw()
