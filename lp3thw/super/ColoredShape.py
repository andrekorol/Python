class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print('Drawing. Setting shape to:', self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print('Drawing. Setting color to:', self.color)
        super().draw()


cs = ColoredShape(color='blue', shapename='square')
cs.draw()
