def left(index):
    return index*2 + 1

def right(index):
    return index*2 + 2

def parent(index):
    return (index + 1) // 2 - 1

def last_with_child(length):
    return length // 2 - 1

        
class MaxHeap:
    def __init__(self, *, max_length=float("inf")):
        self.list = []
        self.length = 0
        self.max_length = max_length
        
    def up(self, index):
        if self.list[index] > self.list[parent(index)] and parent(index) >= 0:
            self.list[index], self.list[parent(index)] = self.list[parent(index)], self.list[index]
            self.up(parent(index))

    def max_value(self):
        if not self.is_empty:
            return self.list[0]

    def insert(self, value):
        if self.is_full() and value < self.max_value():
            self.delete()
        self.list.append(value)
        self.length += 1
        self.up(self.length-1)

    def change(self):
        index_last = self.length - 1
        self.list[0], self.list[index_last] = self.list[index_last], self.list[0]
        self.length -= 1
        self.max_heapify(0)

    def delete(self):
        if self.length == 0:
            raise IndexError("delete from empty heap")
        self.change()
        result = self.list.pop()
        return result

    def max_heapify(self, index):
        l = left(index)
        r = right(index)
        if (l < self.length) and (self.list[l] > self.list[index]):
            largest = l
        else:
            largest = index
        if (r < self.length) and (self.list[r] > self.list[largest]):
            largest = r
        if largest != index:
            self.list[index], self.list[largest] = self.list[largest], self.list[index]
            self.max_heapify(largest)

    def check_invariant(self):
        for i in range(0, last_with_child(self.length)+1):
            check_left = self.list[i] >= self.list[left(i)]
            check_right = self.list[i] >= self.list[right(i)] if right(i) < self.length else True
            if not (check_left and check_right):
                return False
        return True

    @classmethod
    def build_max_heap(cls, array):
        result = cls()
        result.list = array[:]
        result.length = len(result.list)
        indexes = range(0, last_with_child(len(array))+1)
        for i in reversed(indexes):
            result.max_heapify(i)
        return result

    @classmethod
    def sort(cls, array):
        heap = cls.build_max_heap(array)
        while heap.length > 1:
            heap.change()
        return heap.list

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.max_length

    def size(self):
        return self.length

    def __str__(self):
        return str(self.list)


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

    def test_insert():
        array = [12, 1, 5, 6, 3, 7, 15]
        heap = MaxHeap()
        for val in array:
            heap.insert(val)
        assert heap.check_invariant()
        assert len(heap.list) == len(array)
        assert all(val in heap.list for val in array)

        array = [3, 16, 1, 39, 0, 2]
        heap = MaxHeap()
        for val in array:
            heap.insert(val)
        assert heap.check_invariant()
        assert len(heap.list) == len(array)
        assert all(val in heap.list for val in array)
        print("insert ok")

    def test_delete():
        heap = MaxHeap()
        heap.list = [39, 14, 16, 10, 11, 9, 4, 2]
        heap.length = 8
        length_before = heap.length
        assert heap.delete() == 39
        length_after = heap.length
        assert length_before == length_after + 1
        assert heap.check_invariant()

        heap = MaxHeap()
        heap.list = [32, 12, 11, 10, 6, 4, 3]
        heap.length = 7
        length_before = heap.length
        assert heap.delete() == 32
        length_after = heap.length
        assert length_before == length_after + 1
        assert heap.check_invariant()
        print("delete ok")

    def test_max_heapify():
        heap = MaxHeap()
        heap.list = [1, 16, 19, 0, 2, 8, 9, 7]
        heap.length = 8
        heap.max_heapify(0)
        assert heap.list == [19, 16, 9, 0, 2, 8, 1, 7]
        
        heap.list = [7, 16, 9, 8, 15, 0, 20, 3, 1]
        heap.length = 9
        heap.max_heapify(0) 
        assert heap.list == [16, 15, 9, 8, 7, 0, 20, 3, 1]
        
        heap.list = [5, 20, 10, 6, 1, 12]
        heap.length = 6
        heap.max_heapify(2) 
        assert heap.list== [5, 20, 12, 6, 1, 10]
        print("max_heapify ok")

    def test_check_invariant():
        heap = MaxHeap()
        heap.list = [19, 16, 9, 0, 2, 8, 1]
        heap.length = 7
        assert heap.check_invariant()
        heap.list = [1, 16, 19, 0, 2, 8, 9, 7]
        heap.length = 8
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

    def test_sort():
        array = [6, 4, 5, 11, 16, 7]
        result = MaxHeap.sort(array)
        assert result == [4, 5, 6, 7, 11, 16]
        print("sort ok")

    test()
    test_insert()
    test_delete()
    test_max_heapify()
    test_check_invariant()
    test_build_max_heap()
    test_sort()