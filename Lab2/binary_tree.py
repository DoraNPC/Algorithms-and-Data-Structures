class BinaryNode:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def add(self, value):
        if self.key < value:
            if self.right is None:
                self.right = BinaryNode(key=value, parent=self)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = BinaryNode(key=value, parent=self)
            else:
                self.left.add(value)

    def __iter__(self):
        if self.left is not None:
            yield from iter(self.left)
        yield self.key
        if self.right is not None:
            yield from iter(self.right)

    def __str__(self):
        return ' -> '.join(str(key) for key in self)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(key=value)
        else:
            self.root.add(value)
        
    def __iter__(self):
        if self.root is not None:
            return iter(self.root)

    def __str__(self):
        if self.root is not None:
            return str(self.root)

        


if __name__ == "__main__":
    def tests():
        test_iter_node()
        test_add_node()
        test_add_tree()

    def test_iter_node():
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
        print('__iter__ ok')

    def test_add_node():
        node = BinaryNode(4)
        node.add(2)
        node.add(1)
        node.add(3)
        node.add(6)
        node.add(5)
        node.add(7)
        assert str(node) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7"
        print('add_node ok')
    
    def test_add_tree():
        node = BinarySearchTree()
        node.add(4)
        node.add(2)
        node.add(1)
        node.add(3)
        node.add(6)
        node.add(5)
        node.add(7)
        assert str(node) == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7"
        print('add_tree ok')
        

    tests()