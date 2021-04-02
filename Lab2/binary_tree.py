def height(node):
    return node.height if node else -1

class BinaryNode:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.height = 0
        self.parent = parent
        self.left = None
        self.right = None

    def subtree_first(self):
        if self.left:
            return self.left.subtree_first()
        return self

    def subtree_last(self):
        if self.right:
            return self.right.subtree_last()
        return self 

    def predecessor(self):
        if self.left:
            return self.left.subtree_last()
        while self.parent and (self is self.parent.left):
            self = self.parent
        return self.parent

    def successor(self):
        if self.right:
            return self.right.subtree_first()
        while self.parent and (self is self.parent.right):
            self = self.parent
        return self.parent

    def subtree_update(self):
        self.height = 1 + max(height(self.left), height(self.right))

    def skew(self):
        return height(self.right) - height(self.left)

    def subtree_rotate_right(self):
        assert self.left, "No left subtree"
        left = self.left
        self.key, left.key = left.key, self.key
        self.left = left.left
        if left.left:
            left.left.parent = self
        left.left, left.right = left.right, self.right
        if self.right:
            self.right.parent = left
        self.right = left
        left.subtree_update()
        self.subtree_update()

    def subtree_rotate_left(self):
        assert self.right, "No right subtree"
        right = self.right
        self.key, right.key = right.key, self.key
        self.right = right.right
        if right.right:
            right.right.parent = self
        right.right, right.left = right.left, self.left
        if self.left:
            self.left.parent = right
        self.left = right
        right.subtree_update()
        self.subtree_update()

    def rebalance(self):
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):
        self.rebalance()
        self.subtree_update()
        if self.parent:
            self.parent.maintain()

    def subtree_delete(self):
        if self.left or self.right:
            if self.left:
                node = self.predecessor()
            else:
                node = self.successor()
            self.key, node.key = node.key, self.key
            return node.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None 
            self.parent.maintain()
        return self

    def subtree_find(self, value):
        if value == self.key:
            return self
        if value < self.key and self.left:
            return self.left.subtree_find(value)
        if value > self.key and self.right:
            return self.right.subtree_find(value)

    def subtree_add(self, other):
        if other.key < self.key:
            if self.left:
                self.left.subtree_add(other)
            else:
                self.left = other
                other.parent = self
                self.maintain()
        else:
            if self.right:
                self.right.subtree_add(other)
            else:
                self.right = other
                other.parent = self
                self.maintain()
            
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
        self.size = 0

    def add(self, value):
        node = BinaryNode(value)
        if self.root:
            self.root.subtree_add(node)
        else:
            self.root = node
        self.size += 1
        
    def __iter__(self):
        if self.root:
            for node in self.root.subtree_inorder():
                yield node.key

    def __contains__(self, value):
        if self.root:
            node = self.root.subtree_find(value)
            return node is not None

    def __len__(self):
        return self.size

    def search(self, value):
        if value in self:
            return value

    def is_full(self):
        return not self.is_empty()

    def is_empty(self):
        return self.size == 0

    def delete(self, value):
        if self.root:
            node = self.root.subtree_find(value)
            if node:
                deleted = node.subtree_delete()
                if deleted.parent is None:
                    self.root = None
                self.size -= 1
                return value

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
        node = BinaryNode(3)
        a = BinaryNode(2)
        b = BinaryNode(5)
        c = BinaryNode(1)
        d = BinaryNode(4)
        e = BinaryNode(6)
        f = BinaryNode(7)
        node.subtree_add(a)
        node.subtree_add(b)
        node.subtree_add(c)
        node.subtree_add(d)
        node.subtree_add(e)
        node.subtree_add(f)
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
        assert len(node) == 7
        assert node.is_full() == True
        assert node.is_empty() == False
        a = node.delete(7)
        assert a == 7
        assert str(node) == "1 -> 2 -> 3 -> 4 -> 5 -> 6"
        print('add_tree ok')
        

    tests()