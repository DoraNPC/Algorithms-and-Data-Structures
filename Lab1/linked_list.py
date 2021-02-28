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
        print('SortedLinkedList ok')
    

test_node()
test_list()
