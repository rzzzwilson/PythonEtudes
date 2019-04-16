class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree():
    tree = Node(7)
    tree.left = Node(3)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.left.right.left = Node(4)
    tree.left.right.right = Node(6)
    tree.right = Node(8)
    tree.right.right = Node(9)
    return tree

def Xwalk_inorder(node):
    if node:
        walk_inorder(node.left)
        print(node.value)
        walk_inorder(node.right)

def walk_inorder(node, history=None):
    """Return a list of node values from an in-order walk of the tree."""

    if history is None:
        history = []
    if node:
        history = walk_inorder(node.left, history)
        history.append(node.value)
        history = walk_inorder(node.right, history)
    return history

def reverse_tree(node):
    if node:
        reverse_tree(node.left)
        reverse_tree(node.right)
        (node.left, node.right) = (node.right, node.left)

tree = create_tree()
order_before = walk_inorder(tree)
print(order_before)
reverse_tree(tree)
order_after = walk_inorder(tree)
print(order_after)
if order_before != list(reversed(order_after)):
    print('Error!')

