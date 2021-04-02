class BinaryNode:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def subtree_find(self, value):
        if value == self.key:
            return self
        if value < self.key and self.left:
            return self.left.subtree_find(value)
        if value > self.key and self.right:
            return self.right.subtree_find(value)

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
            
    def subtree_preorder(self):
        yield self
        if self.left:
            yield from self.left.subtree_preorder()
        if self.right:
            yield from self.right.subtree_preorder()

    def subtree_inorder(self):
        if self.left:
            yield from self.left.subtree_inorder()
        yield self
        if self.right:
            yield from self.right.subtree_inorder()

    def subtree_postorder(self):
        if self.left:
            yield from self.left.subtree_postorder()
        if self.right:
            yield from self.right.subtree_postorder()
        yield self

    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = BinaryNode(key=value)
        else:
            self.root.add(value)
        
    def __iter__(self):
        if self.root:
            for node in self.root.subtree_inorder():
                yield node.key

    def __contains__(self, value):
        if self.root:
            node = self.root.subtree_find(value)
            return node is not None

    def __len__(self):
        raise NotImplementedError

    def search(self, value):
        if value in self:
            return value

    def is_full(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def delete(self, value):
        raise NotImplementedError

    def detour(self, order):
        if self.root:
            if order == 'preorder':
                iterator = self.root.subtree_preorder()
            elif order == 'inorder':
                iterator = iter(self)
            elif order == 'postorder':
                iterator = self.root.subtree_postorder()
            else:
                raise ValueError
            return ' -> '.join(str(x) for x in iterator) 

    def __str__(self):
        if self.root:
            return ' -> '.join(str(x) for x in self.root.subtree_inorder()) 
   

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
        assert [str(x) for x in d.subtree_inorder()] == ['1', '2', '3', '4', '5', '6', '7']
        assert [str(x) for x in d.subtree_postorder()] == ['1', '3', '2', '5', '7', '6', '4']
        assert [str(x) for x in d.subtree_preorder()] == ['4', '2', '1', '3', '6', '5', '7']
        print('__iter__ ok')

    def test_add_node():
        node = BinaryNode(4)
        node.add(2)
        node.add(1)
        node.add(3)
        node.add(6)
        node.add(5)
        node.add(7)
        assert [str(x) for x in node.subtree_inorder()] == ['1', '2', '3', '4', '5', '6', '7']
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
        assert node.detour('inorder') == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7"
        assert node.detour('postorder') == "1 -> 3 -> 2 -> 5 -> 7 -> 6 -> 4"
        assert node.detour('preorder') == "4 -> 2 -> 1 -> 3 -> 6 -> 5 -> 7"
        assert 8 not in node
        assert 2 in node
        assert node.search(3) == 3
        assert node.search(9) is None
        print('add_tree ok')
        

    tests()