from linked_list import SortedLinkedList
my_list = SortedLinkedList()
my_list.add(4)
my_list.add(6)
my_list.add(9)
my_list.add(5)
print(f'my_list: {my_list}')
print(f'Is 5 in my list: {5 in my_list}')
print(f'Is 19 in my list: {19 in my_list}')
print(f'sum of even: {my_list.sum_items()}')
my_list.delete(9)
my_list.delete(5)
print(f'list after delete 9 and 5: {my_list}')