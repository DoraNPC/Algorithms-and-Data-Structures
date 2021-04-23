import heap
a = heap.MaxHeap(max_length=6)
arr1 = [11, 34, 1, 5, 4, 48, 37, 19, 56, 9, 2, 8, 0, 35, 7, 30, 78]
for i in arr1:
    a.insert(i)
print(f"6 min values in heap: {a}")
a.delete()
print(f"Heap after deleting largest element: {a}")
print(f"Is full: {a.is_full()}")
print (f"Is empty: {a.is_empty()}")

b = heap.MaxHeap()
arr2 = [5, 7, 8, 2, 88, 34, 68, 43, 89]
for i in arr2:
    b.insert(i)
print(f"Max value in heap: {b.max_value()}")
print(f"Heap sorted: {heap.MaxHeap.sort(arr2)}")
print(f"Printed heap{b.list}")
print(f"Find k min: {heap.MaxHeap.find_k_min(arr2, 4)}")
print(f"Find k min: {heap.MaxHeap.find_k_min2(arr2, 4)}")
print(f"Find k max: {heap.MaxHeap.find_k_max(arr2, 4)}")