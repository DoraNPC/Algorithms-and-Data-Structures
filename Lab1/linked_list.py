class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)


class SortedLinkedList:
    def __init__(self):
        """Create empty list"""
        self.head = None
        self.tale = None
        self.length = 0

    def add(self, value):
        """Add element"""
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tale = node
        elif value <= self.head.value:
            node.link = self.head
            self.head = node
        elif value >= self.tale.value:
            self.tale.link = node
            self.tale = node
        else:
            prev = self.head
            next = self.head.link
            while next.value < value:
                prev = next
                next = next.link
            prev.link = node
            node.link = next
        self.length += 1

    def delete(self, value):
        """Delete value and return it"""
        if len(self) == 0:
            return
        if self.head.value <= value <= self.tale.value:
            if len(self) == 1:
                self.head = None
                self.tale = None
            elif self.head.value == value:
                self.head = self.head.link
            else: 
                prev = self.head
                while prev.link.value < value:
                    prev = prev.link
                if prev.link.value > value:
                    return
                else:
                    if prev.link == self.tale:
                        self.tale = prev
                    prev.link = prev.link.link
            self.length -=1
            return value
            
    def __iter__(self):
        """Return iterator"""
        node = self.head
        while node:
            yield node.value
            node = node.link

    def __str__(self):
        """List output"""
        node = self.head
        result = []
        while node:
            result.append(str(node.value))
            node = node.link
        return '-->'.join(result)

    def __len__(self):
        """Return list size"""
        return self.length

    def is_empty(self):
        """Check if list is empty"""
        return self.length == 0


if __name__ == '__main__':
    def test_node():
        node = Node(2)
        assert node.value == 2 and node.link is None
        node1 = Node(34)
        node2 = Node(8)
        node.link = node1
        node1.link = node2
        assert node.link == node1 
        assert node1.value == 34 and node1.link == node2 
        assert node2.value == 8 and node2.link == None
        print('Node ok')

    def test_list():
        linked_list = SortedLinkedList()
        assert len(linked_list) == 0
        assert linked_list.is_empty()
        linked_list.add(4)
        linked_list.add(5)
        linked_list.add(46)
        linked_list.add(12)
        linked_list.add(2)
        assert str(linked_list) == '2-->4-->5-->12-->46'
        assert len(linked_list) == 5
        assert not linked_list.is_empty()
        a = linked_list.delete(1)
        assert a is None and len(linked_list) == 5
        a = linked_list.delete(2)
        assert a == 2 and len(linked_list) == 4
        assert str(linked_list) == '4-->5-->12-->46'
        a = linked_list.delete(52)
        assert a is None and len(linked_list) == 4
        a = linked_list.delete(46)
        assert a == 46 and len(linked_list) == 3
        assert str(linked_list) == '4-->5-->12'
        a = linked_list.delete(6)
        assert a is None and len(linked_list) == 3
        a = linked_list.delete(5)
        assert a == 5 and len(linked_list) == 2
        assert str(linked_list) == '4-->12'
        print('SortedLinkedList ok')

    def test_delete():
        linked_list = SortedLinkedList()
        linked_list.add(2)
        linked_list.delete(2) 
        assert len(linked_list) == 0
        print('Delete ok')

    def test_iter():
        linked_list = SortedLinkedList()
        linked_list.add(4)
        linked_list.add(5)
        linked_list.add(46)
        linked_list.add(12)
        linked_list.add(2)
        assert list(linked_list) == [2, 4, 5, 12, 46]
        print('Iter ok')

    def input_check():
        linked_list = SortedLinkedList()
        linked_list.add(4)
        linked_list.add(5)
        linked_list.add(46)
        linked_list.add(12)
        linked_list.add(2)
        assert 2 in linked_list
        assert not 8 in linked_list
        print('Input check ok')
    

test_node()
test_list()
test_delete()
test_iter()
input_check()
