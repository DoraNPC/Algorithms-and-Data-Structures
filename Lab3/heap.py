def left(index):
    return index*2 + 1

def right(index):
    return index*2 + 2

def parent(index):
    return (index + 1) // 2 - 1

def last_with_child(length):
    return length // 2 - 1

class MaxHeap:
    def __init__(self):
        self.list = []

    def max_heapify(self, index):
        l = left(index)
        r = right(index)
        if (l < len(self.list)) and (self.list[l] > self.list[index]):
            largest = l
        else:
            largest = index
        if (r < len(self.list)) and (self.list[r] > self.list[largest]):
            largest = r
        if largest != index:
            self.list[index], self.list[largest] = self.list[largest], self.list[index]
            self.max_heapify(largest)

    def check_invariant(self):
        for i in range(0, last_with_child(len(self.list)+1)):
            if self.list[i] < self.list[left(i)] or self.list[i] < self.list[right(i)]:
                return False
        return True

    @classmethod
    def build_max_heap(cls, array):
        result = cls()
        result.list = array[:]
        indexes = range(0, last_with_child(len(array)+1))
        for i in reversed(indexes):
            result.max_heapify(i)
        return result


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

    def test_max_heap():
        heap = MaxHeap()
        heap.list = [1, 16, 19, 0, 2, 8, 9, 7]
        heap.max_heapify(0)
        assert heap.list == [19, 16, 9, 0, 2, 8, 1, 7]
        
        heap.list = [7, 16, 9, 8, 15, 0, 20, 3, 1]
        heap.max_heapify(0) 
        assert heap.list == [16, 15, 9, 8, 7, 0, 20, 3, 1]
        
        heap.list = [5, 20, 10, 6, 1, 12]
        heap.max_heapify(2) 
        assert heap.list== [5, 20, 12, 6, 1, 10]
        print("max_heapify ok")

    def test_check_invariant():
        heap = MaxHeap()
        heap.list = [19, 16, 9, 0, 2, 8, 1, 7]
        assert heap.check_invariant()
        heap.list = [1, 16, 19, 0, 2, 8, 9, 7]
        assert not heap.check_invariant()
        print("check_invariant ok")

    def test_build_max_heap():
        array = [1, 6, 12, 8, 33, 6, 3]
        result = MaxHeap.build_max_heap(array)
        assert result.check_invariant()

        array = [6, 1, 3, 49, 55, 8]
        result = MaxHeap.build_max_heap(array)
        assert result.check_invariant()

        array = [22, 14, 2, 6, 11, 0]
        result = MaxHeap.build_max_heap(array)
        assert result.check_invariant()
        print("build_max_heap ok")

    test()
    test_max_heap()
    test_check_invariant()
    test_build_max_heap()
    