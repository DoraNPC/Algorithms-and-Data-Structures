class BinaryNode:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def __iter__(self):
        if self.left is not None:
            yield from iter(self.left)
        yield self.key
        if self.right is not None:
            yield from iter(self.right)
            
    def __str__(self):
        return ' -> '.join(str(key) for key in self)


if __name__ == "__main__":
    def tests():
        test_node()

    def test_node():
        a = BinaryNode(1)
        b = BinaryNode(2)
        c = BinaryNode(3)
        d = BinaryNode(4)
        e = BinaryNode(5)
        f = BinaryNode(6)
        g = BinaryNode(7)
        d.left = b
        d.right = f
        b.parent = d
        b.left = a
        b.right = c
        a.parent = b
        c.parent = b
        f.parent = d
        f.left = e
        f.right = g
        e.parent = f
        g.parent = f
        assert str(d) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7"
        print('Binary node ok')

    tests()