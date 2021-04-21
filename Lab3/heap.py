def left(index):
    result = index * 2 + 1
    return result

def right(index):
    result = index*2 + 2
    return result

def parent(index):
    return (index + 1) // 2 - 1
    return result

class Heap:
    def __init__(self):
        self.list = []


if __name__ == "__main__":
    def test():
        assert left(0) == 1
        assert left(1) == 3
        assert left(2) == 5
        assert left(5) == 11
        assert left(4) == 9
        assert left(100) == 201
        assert left(99) == 199
        print('left ok')

        assert right(1) == 4
        assert right(2) == 6
        assert right(5) == 12
        assert right(6) == 14
        assert right(3) == 8
        assert right(100) == 202
        assert right(99) == 200
        print('right ok')

        assert parent(2) == 0
        assert parent(5) == 2
        assert parent(10) == 4
        assert parent(100) == 49
        assert parent(99) == 49
        
        print('parent ok')
    test()
