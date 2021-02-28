class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)


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

test_node()