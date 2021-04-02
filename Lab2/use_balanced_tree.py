from binary_tree import BinarySearchTree

tree = BinarySearchTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
tree.add(6)
tree.add(7)
tree.add(8)

print(f'Balanced tree: {str(tree)}')
print(f'Tree is empty: {tree.is_empty()}')
print(f'Is 7 in this tree: {7 in tree}')
print(f'If 5 in this tree return it: {tree.search(5)}')
print(f'Tree root: {tree.root.key}')

tree.delete(4)
tree.delete(6)
print(f'After deleting 4 and 6: {str(tree)}')

print(f'Tree length: {len(tree)}')

print(f'Left subtree height: {tree.root.left.height}')
print(f'Right subtree height: {tree.root.right.height}')


print(f'Inorder: {tree.detour("inorder")}')
print(f'Preorder: {tree.detour("preorder")}')
print(f'Postorder: {tree.detour("postorder")}')

print(f'Tree root: {tree.root.key}')
